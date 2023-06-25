import random
import copy


def get_random_assignment(slots):
    assignments = {
        day: {
            st: [None, None]
            for st in slots[day]
        } for day in slots
    }
    for day in slots:
        for st in slots[day]:
            if slots[day][st]:
                # sample 2 for 매표소, 수영장
                if (len(slots[day][st]) == 1):
                    assignments[day][st][0] = slots[day][st][0]
                else:
                    assignments[day][st] = sorted(
                        random.sample(slots[day][st], 2))
    return assignments


def mutate_assignment(assignments, slots):
    mutant = copy.deepcopy(assignments)
    for day in slots:
        for st in slots[day]:
            if slots[day][st]:
                if random.random() < 0.1:
                    # mutate 10%
                    if (len(slots[day][st]) == 1):
                        assignments[day][st][0] = slots[day][st][0]
                    else:
                        assignments[day][st] = sorted(
                            random.sample(slots[day][st], 2))
    return mutant


def crossover_assignments(assignments1, assignments2):
    mutant = {}
    for day in assignments1:
        if random.random() < 0.5:
            mutant[day] = copy.deepcopy(assignments1[day])
        else:
            mutant[day] = copy.deepcopy(assignments2[day])
    return mutant


def slot_overlaps(slot1, slot2) -> bool:
    assert (len(slot1) == len(slot2) == 2)
    return slot1[0] in slot2 or slot1[1] in slot2


def num_fragments(seq):
    # TODO: is this penalty?
    count = 1
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            count += 1
    return count


def calc_penalty_consecutive_inner(frags: list) -> int:
    assert (len(frags) == 2)
    if frags[0] == 1 or frags[1] == 1:
        # 30분에 패널티
        return 10
    elif (frags[0] is not None and frags[0] > 8) or (frags[1] is not None and frags[1] > 8):
        # 4시간 이상에 패널티
        return 1
    else:
        return 0


def calc_penalty_consecutive(seq):
    len_fragments = [[None, None]]
    for i in range(1, len(seq)):
        if len_fragments[-1][0] is None and seq[i][0] is not None:
            len_fragments[-1][0] = 1
        if len_fragments[-1][1] is None and seq[i][1] is not None:
            len_fragments[-1][1] = 1

        if len_fragments[-1][0] is not None and seq[i-1][0] in seq[i]:
            if seq[i-1][0] == seq[i][0]:
                len_fragments[-1][0] += 1
            else:
                len_fragments[-1][1] += 1
        if len_fragments[-1][0] is not None and seq[i-1][1] in seq[i]:
            if seq[i-1][1] == seq[i][0]:
                len_fragments[-1][0] += 1
            else:
                len_fragments[-1][1] += 1

        to_append = False
        append0 = len_fragments[-1][0]
        append1 = len_fragments[-1][1]
        if seq[i][0] is None:
            to_append = True
            append0 = None
        if seq[i][1] is None:
            to_append = True
            append1 = None
        if seq[i-1][0] not in seq[i]:
            to_append = True
            append0 = 1
        if seq[i-1][1] not in seq[i]:
            to_append = True
            append1 = 1

        if to_append:
            len_fragments.append([append0, append1])

    return sum(list(map(calc_penalty_consecutive_inner, len_fragments)))


def compute_fitness(assignments, ideal_ratio, alpha=0.5, verbose=False):
    fragment_fitness = 0
    ratio_fitness = 0
    # penalty
    for day in assignments:
        assignees = [assignments[day][st] for st in assignments[day]]
        fragment_fitness += calc_penalty_consecutive(assignees)

    actual_ratio = {person: 0 for person in ideal_ratio}
    for day in assignments:
        for people in assignments[day].values():
            if people is None:
                continue
            if people[0] is not None:
                actual_ratio[people[0]] += 1
            if people[1] is not None:
                actual_ratio[people[1]] += 1

    total = sum(actual_ratio.values())
    for person in actual_ratio:
        actual_ratio[person] /= total

    if verbose:
        print(f"name\tideal\tactual")
    for person in actual_ratio:
        ratio_fitness += abs(ideal_ratio[person]
                             - actual_ratio[person])
        if verbose:
            print(
                f"{person}\t{ideal_ratio[person]:.3f}\t{actual_ratio[person]:.3f}")

    return alpha * fragment_fitness + (1 - alpha) * ratio_fitness


def get_best_n(populations, n, ideal_ratio, alpha):
    fitnesses = []
    for individual in populations:
        fitnesses.append((
            compute_fitness(individual, ideal_ratio, alpha),
            individual
        ))
    fitnesses = sorted(fitnesses, key=lambda t: t[0])
    return [i for _, i in fitnesses[:n]]
