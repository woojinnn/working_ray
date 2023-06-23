from typing import Dict, List, Tuple

import gspread


def init_table(sh: gspread.Spreadsheet, slots: Dict[str, Dict[int, list]]):
    worksheet = sh.add_worksheet(title='근로시간표', rows=18, cols=9)
    