from typing import Dict, List

import gspread
import json

SCOPES = ['https://accounts.google.com/o/oauth2/token',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://spreadsheets.google.com/feeds',
          ]
SERVICE_ACCOUNT_FILE = '/home/woojin/Desktop/kaori-worker-ca7a53ab02da.json'
KEY_PATH = '/home/woojin/Desktop/client_secret_626783014254-6a3mkqcflmuf9btuqrkg3qntgqtrop9h.apps.googleusercontent.com.json'


def parse_input(filepath: str) -> Dict[str, Dict[str, list]]:
    available = {}
    with open(filepath, "r") as f:
        for l in f:
            if not l.strip():
                continue
            if l.startswith("- "):
                person: str = l.strip().split()[-1]
                available[person] = {}
            else:
                day = l.strip().split(":")[0]
                slots = [tuple(map(float, rg.split("-")))
                         for rg in l.strip().split(":")[1].split(",")]
                available[person][day] = slots
    return available


def get_worksheets(url_info: str) -> List[gspread.Worksheet]:
    """
    get_worksheets

    # Load Google sheet information
    # FYI:
    # - <http://urin79.com/blog/20667833>
    # - <https://greeksharifa.github.io/references/2023/04/10/gspread-usage/>
    # - <https://velog.io/@chaejm55/%EA%B5%AC%EA%B8%80-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EC%8B%9C%ED%8A%B8-%EC%9E%90%EB%8F%99%ED%99%945-%EC%99%B8%EB%B6%80-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%A1%9C-%EC%9E%90%EB%8F%99%ED%99%94-%ED%95%98%EA%B8%B0>
    """
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open_by_url(url_info)

    # Get the first sheet
    # Assuming the responses are on the first sheet
    worksheet_list = sh.worksheets()

    return worksheet_list


def get_responses(worksheet: gspread.Worksheet) -> Dict[str, Dict[str, list]]:
    col_names = worksheet.row_values(1)
    name_col_idx = col_names.index("이름")

    values_dicts: List[Dict[str, str]] = worksheet.get_all_records()

    return


if __name__ == "__main__":
    # test form url: <https://forms.gle/jQJUTPZDhGPKyuz29>
    worksheets = get_worksheets(
        "https://docs.google.com/spreadsheets/d/1J4XB5QY8QFIkWRAa5fMjgGmZNYB_uxwQQEixpmYgLes/edit?resourcekey#gid=345720317")
    for worksheet in worksheets:
        print(worksheet.title)
        get_responses(worksheet)
