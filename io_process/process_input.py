from typing import Dict, List

import gspread
from google.oauth2 import service_account
import json
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import Flow

SCOPES = ['https://accounts.google.com/o/oauth2/token',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/forms',
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

# Load the Load the responses from the Google Form
# FIXME: Current version is just copied from GPT answer
# FYI:
# - <http://urin79.com/blog/20667833>
# - <https://greeksharifa.github.io/references/2023/04/10/gspread-usage/>
def crawl_responses(form_name: str) -> List[Dict[str, str]]:
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open("근로_test(응답)")

    # Get the first sheet
    # Assuming the responses are on the first sheet
    sheet = sh.get_worksheet(0)

    # Fetch all values
    values = sheet.get_all_values()

    # Process the values
    for row in values:
        # Each row represents a form response
        # Process the data as per your requirements
        print(row)  # Example: print the entire row
