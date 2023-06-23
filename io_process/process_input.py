from typing import Dict, List

import gspread
from google.oauth2.service_account import Credentials


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
    # TODO: Setup Google API credentials:
    # 1. Go to the Google Developers Console.
    # 2. Create a new project or select an existing project.
    # 3. Enable the "Google Sheets API" for your project.
    # 4. Create credentials (OAuth client ID) and download the JSON file.

    # Load the credentials from the JSON file
    # FIXME
    credentials = Credentials.from_service_account_file(
        'path/to/credentials.json')

    # Authorize the client
    client = gspread.authorize(credentials)

    # Open the Google Form responses spreadsheet
    # FIXME
    # Replace with the name of your form's responses spreadsheet
    spreadsheet = client.open('Form Responses')

    # Get the first sheet
    # Assuming the responses are on the first sheet
    sheet = spreadsheet.get_worksheet(0)

    # Fetch all values
    values = sheet.get_all_values()

    # Process the values
    for row in values:
        # Each row represents a form response
        # Process the data as per your requirements
        print(row)  # Example: print the entire row
