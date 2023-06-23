from typing import Dict, List

import random
import pandas as pd
import argparse
from tqdm import tqdm

from io_process import process_input as inp
import ga

# ========================== edit here ========================
START_TIME = 8
END_TIME = 21
UNIT = 0.5    # 1 hour
# UNIT = 0.5 # 30 mins
DAYS = ["월", "화", "수", "목", "금"]

# Genetic algorithm hyperparameter
NUM_POPULATIONS = 50
NUM_GENERATIONS = 100
NUM_ELITES = 10
ALPHA = 0.7  # [0, 1] 0에 가까울 수록 분배 우선, 1에 가까울 수록 연속적 배정 우선
# ==============================================================

# glob vars
SLOT_START_TIMES: List[int] = [
    START_TIME + UNIT*i for i in range(int((END_TIME - START_TIME)/UNIT))
]


def fill_slots(slots, available):
    for person in available:
        for day in available[person]:
            for start_t, end_t in available[person][day]:
                for st in SLOT_START_TIMES:
                    if st >= start_t and st+UNIT <= end_t:
                        slots[day][st].append(person)
    return slots


def get_ideal_ratio(available):
    ideal_ratio = {}
    for person in available:
        amount = 0
        for day in available[person]:
            for st, et in available[person][day]:
                amount += et - st
        ideal_ratio[person] = amount
    total = sum(ideal_ratio.values())
    for person in ideal_ratio:
        ideal_ratio[person] /= total
    return ideal_ratio


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', type=int, default=3)
    parser.add_argument('-o', type=str, default="timetable")

    args = parser.parse_args()

    slots = {
        day: {
            st: []
            for st in SLOT_START_TIMES
        } for day in DAYS
    }

    available = inp.parse_input("https://docs.google.com/spreadsheets/d/1qyeYJX2HHHhvsU9X5uCd1VzGI9Tp801-y3rCzlhk3Ww/edit?resourcekey#gid=1866203138")
    fill_slots(slots, available)
    ideal_ratio = get_ideal_ratio(available)

    # initial population
    populations = [
        ga.get_random_assignment(slots)
        for _ in range(NUM_POPULATIONS)
    ]

    print("Scheduling using GA...")
    for gen in tqdm(range(NUM_GENERATIONS), colour="blue"):
        elites = ga.get_best_n(populations, NUM_ELITES,
                                ideal_ratio, alpha=ALPHA)
        new_populations = []
        for i in range(NUM_POPULATIONS - NUM_ELITES):
            if random.random() < 0.5:
                new_populations.append(ga.mutate_assignment(
                    random.choice(elites), slots))
            else:
                new_populations.append(ga.crossover_assignments(
                    *random.choices(elites, k=2)))
        populations = elites + new_populations
        assert len(populations) == NUM_POPULATIONS
    print("Done")

    best_individuals = ga.get_best_n(
        populations, args.n, ideal_ratio, alpha=ALPHA)

    for i in range(args.n):
        assignments = best_individuals[i]
        rows = []
        print(f"=================== Option #{i+1} ===================")
        print()
        ga.compute_fitness(assignments, ideal_ratio, verbose=True)
        for day in assignments:
            for st in assignments[day]:
                rows.append([day, st, assignments[day][st]])
        df = pd.DataFrame(data=rows,
                            columns=["day", "start_time", "assignee"]
                            ).pivot(index="start_time", columns="day", values="assignee")
        print()
        print(df[DAYS].to_markdown())
        df[DAYS].to_csv(f"{args.o}_{i}.csv")
        print()
