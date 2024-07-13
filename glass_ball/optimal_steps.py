def throw_ball(curr_floor: int, breaking_floor: int) -> bool:
    return curr_floor >= breaking_floor


def get_optimal_step(starting_floor: int, ending_floor: int):
    step = 1
    while step * (step + 1) // 2 < (ending_floor - starting_floor): # int(math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2))
        step += 1
    return step


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int) -> tuple:
    attempts = 0
    broken_balls = 0
    step = get_optimal_step(starting_floor, ending_floor)
    curr_floor = starting_floor


    while curr_floor <= ending_floor:
        curr_floor += step
        step -= 1

        attempts += 1
        if throw_ball(curr_floor, breaking_floor):
            broken_balls += 1
            break

    # floor limit rounder
    if curr_floor > ending_floor:
        curr_floor = ending_floor

    for floor in range(curr_floor - step, curr_floor + 1):
        attempts += 1
        if throw_ball(floor, breaking_floor):
            broken_balls += 1
            return attempts, broken_balls, floor

    return attempts, broken_balls, ending_floor