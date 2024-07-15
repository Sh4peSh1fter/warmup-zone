# Imports
import math
from config import setup_module_logger
from config import Result


# Logging
logger = setup_module_logger(__name__)


def throw_ball(curr_floor: int, breaking_floor: int) -> bool:
    # DEBUG
    logger.debug(f'throw and check if the ball breaks\n'
                 f'\twill the ball break? {curr_floor >= breaking_floor}')

    return curr_floor >= breaking_floor


def get_optimal_step(starting_floor: int, ending_floor: int) -> int:
    return math.ceil((-1 + math.sqrt(1 + 8 * (ending_floor - starting_floor + 1))) / 2)


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int) -> Result:
    step_size = get_optimal_step(starting_floor, ending_floor)
    curr_floor = step_size * math.floor((ending_floor - starting_floor) // 2 // step_size)
    broken_balls = 0
    attempts = 0

    # DEBUG
    logger.debug(f"setup\n"
                 f"\tgenerated breaking floor: {breaking_floor}\n"
                 f"\tstarting floor: {curr_floor}\n"
                 f"\toptimal step: {step_size}")

    # set broke_last_floor
    if throw_ball(curr_floor, breaking_floor):
        broke_last_floor = True
    else:
        broke_last_floor = False

    while attempts < 20:
        curr_ball_broke = throw_ball(curr_floor, breaking_floor)
        attempts += 1
        # DEBUG
        logger.debug(f"throwing\n"
                     f"\tattempt number {attempts}\n"
                     f"\tcurrent floor: {curr_floor}\n"
                     f"\tstep size: {step_size}")

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
            broken_balls += 1

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

    # DEBUG
    logger.debug(f'result\n'
                 f'\tattempts: {attempts}\n'
                 f'\tbroken balls: {broken_balls}\n'
                 f'\tbreaking floor guessed: {ending_floor}\n'
                 f'\n--------------------------\n')
    return Result(attempts, broken_balls, curr_floor)