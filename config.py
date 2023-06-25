from typing import List, Dict

START_TIME = 8
END_TIME = 21
# UNIT = 1    # 1 hour
UNIT = 0.5  # 30 mins
DAYS = ["월", "화", "수", "목", "금"]
WORK_TYPE = ["매표소", "수영장"]

# Genetic algorithm hyperparameter
NUM_POPULATIONS = 100
NUM_GENERATIONS = 700
NUM_ELITES = 10
ALPHA = 0.9  # [0, 1] 0에 가까울 수록 분배 우선, 1에 가까울 수록 연속적 배정 우선
# ==============================================================

# glob vars
SLOT_START_TIMES: List[float] = [
    START_TIME + UNIT*i for i in range(int((END_TIME - START_TIME)/UNIT))
]
SLOTS: Dict[str, Dict[int, list]] = {
    day: {
        st: []
        for st in SLOT_START_TIMES
    } for day in DAYS
}


SCOPES = ['https://accounts.google.com/o/oauth2/token',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://spreadsheets.google.com/feeds',
          ]
# SERVICE_ACCOUNT_FILE = '/home/woojin/Desktop/kaori-worker-ca7a53ab02da.json'
# SERVICE_ACCOUNT_FILE = '/home/woojin/kaori-worker-a85899e5e9cc.json'
SERVICE_ACCOUNT_FILE = '/home/woojin/kaori-worker-c15b57a2ea16.json'
KEY_PATH = '/home/woojin/Desktop/client_secret_626783014254-6a3mkqcflmuf9btuqrkg3qntgqtrop9h.apps.googleusercontent.com.json'
RESPONSE_URL = "https://docs.google.com/spreadsheets/d/1siBptWFERpZHyJqISW2iESiNgWfP7EZsh2K4r8cNL2E/edit?resourcekey#gid=1789325319"
