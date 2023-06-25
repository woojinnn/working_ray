from typing import Dict, List, Tuple

from config import *

import pandas as pd
import gspread


def get_spreadsheet(url_inf: str) -> gspread.Spreadsheet:
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open_by_url(url_inf)
    return sh


def parse_time(time_str: str) -> List[tuple]:
    # Currently, input is regulated with the following format:
    # ^(?:8|9|1[0-9]|2[0-1])(?:\.5)?(?:\s*)-(?:\s*)(?:8|9|1[0-9]|2[0-1])(?:\.5)?(?:,(?:\s*)((?:8|9|1[0-9]|2[0-1])(?:\.5)?(?:\s*)-(?:\s*)(?:8|9|1[0-9]|2[0-1])(?:\.5)?))?$

    # TODO
    # add validation logic
    return [tuple(map(float, rg.split("-")))
            for rg in time_str.strip().split(",")]


def visualize_responses(sh: gspread.Spreadsheet, slots):
    sheet_title = "응답 정리"

    rows = []
    for day, v in slots.items():
        for time, people in v.items():
            rows.append([day, time, ', '.join(people)])
    df = pd.DataFrame(data=rows, columns=["day", "start_time", "available"])
    df = df.pivot(index="start_time", columns="day", values="available")
    df = df.reindex(columns=DAYS)

    if sheet_title in [ws.title for ws in sh.worksheets()]:
        result_ws = sh.worksheet(sheet_title)
        sh.del_worksheet(result_ws)
    result_ws = sh.add_worksheet(title=sheet_title, rows=200, cols=30)
    result_ws.update(
        'A3:A200',
        [[f"{START_TIME + UNIT*i}~{START_TIME + UNIT*(i+1)}"] for i in range(
            int((END_TIME - START_TIME)/UNIT))]
    )
    result_ws.update(
        'B2:Z200',
        [df.columns.values.tolist()] + df.values.tolist())


def get_responses(sh: gspread.Spreadsheet) -> Dict[str, Dict[str, list]]:
    worksheet = sh.worksheets()[0]
    values_dicts: List[Dict[str, str]] = worksheet.get_all_records()

    ans = {}
    for resp in values_dicts:
        name = resp["이름"]
        ans[name] = {}
        for k, v in resp.items():
            if not v.strip():
                continue
            if "월" in k:
                ans[name]["월"] = parse_time(v)
            elif "화" in k:
                ans[name]["화"] = parse_time(v)
            elif "수" in k:
                ans[name]["수"] = parse_time(v)
            elif "목" in k:
                ans[name]["목"] = parse_time(v)
            elif "금" in k:
                ans[name]["금"] = parse_time(v)

    return ans


if __name__ == "__main__":
    # test form url: <https://forms.gle/jQJUTPZDhGPKyuz29>
    worksheets = get_worksheets(
        "https://docs.google.com/spreadsheets/d/1qyeYJX2HHHhvsU9X5uCd1VzGI9Tp801-y3rCzlhk3Ww/edit?resourcekey#gid=1866203138")
    for worksheet in worksheets:
        print(worksheet.title)
        resp = get_responses(worksheet)
        print(resp)
