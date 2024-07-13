from random import randrange
import math


def throw_ball(curr_floor: int, breaking_floor: int) -> bool:
    return curr_floor >= breaking_floor


def get_optimal_step(starting_floor: int, ending_floor: int):
    step = 1
    while step * (step + 1) // 2 < (ending_floor - starting_floor):
        step += 1
    return step


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int) -> tuple:
    step_size = get_optimal_step(starting_floor, ending_floor)
    curr_floor = step_size * math.floor((ending_floor - starting_floor) // 2 // step_size)
    glass_balls_broken = 0
    attempts = 0

    # # DEBUG
    # print(f"SETUP:\n"
    #       f"generated breaking floor: {breaking_floor}\n"
    #       f"starting floor: {curr_floor}\n"
    #       f"optimal step: {step_size}\n\n")

    # set broke_last_floor
    if throw_ball(curr_floor, breaking_floor):
        broke_last_floor = True
    else:
        broke_last_floor = False

    while attempts < 30:
        curr_ball_broke = throw_ball(curr_floor, breaking_floor)
        attempts += 1
        # # DEBUG
        # print(f"----------------------------\n"
        #       f"attempt number {attempts}   \n"
        #       f"current floor: {curr_floor} \n"
        #       f"step size: {step_size}      \n"
        #       f"throwing the ball from the {curr_floor} floor.\n"
        #       f"did it break? {curr_ball_broke}")

        if not curr_ball_broke:
            if curr_floor == ending_floor:
                raise ValueError("the ball didnt break in the top floor")
            elif not broke_last_floor:
                curr_floor += step_size
            elif broke_last_floor:
                step_size = math.floor(step_size // 2)
                curr_floor += step_size

            broke_last_floor = False
        elif curr_ball_broke:
            glass_balls_broken += 1

            if not broke_last_floor:
                if step_size == 1:
                    break
                step_size = math.floor(step_size // 2)
                curr_floor -= step_size
            elif broke_last_floor:
                curr_floor -= step_size

            broke_last_floor = True

        # floor rounder
        if curr_floor > ending_floor:
            curr_floor = ending_floor
        elif curr_floor < starting_floor:
            curr_floor = starting_floor
        # step rounder
        if step_size < 1:
            step_size = 1

        # # DEBUG
        # print(f"----------------------------")
    return attempts, glass_balls_broken, curr_floor