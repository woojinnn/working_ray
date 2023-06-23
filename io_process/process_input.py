from typing import Dict, List, Tuple

import gspread

SCOPES = ['https://accounts.google.com/o/oauth2/token',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://spreadsheets.google.com/feeds',
          ]
# SERVICE_ACCOUNT_FILE = '/home/woojin/Desktop/kaori-worker-ca7a53ab02da.json'
SERVICE_ACCOUNT_FILE = '/home/woojin/kaori-worker-a85899e5e9cc.json'
KEY_PATH = '/home/woojin/Desktop/client_secret_626783014254-6a3mkqcflmuf9btuqrkg3qntgqtrop9h.apps.googleusercontent.com.json'


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
