# Imports
import math
from config import setup_module_logger
from config import Result


# Logging
logger = setup_module_logger(__name__)

def throw_ball(curr_floor: int, breaking_floor: int) -> bool:
    # DEBUG
    logger.debug(f'throw and check if the item breaks\n'
                 f'\twill the item break? {curr_floor >= breaking_floor}')

    return curr_floor >= breaking_floor


def get_optimal_step(starting_floor: int, ending_floor: int) -> int:
    return math.ceil((-1 + math.sqrt(1 + 8 * (ending_floor - starting_floor + 1))) / 2)


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int) -> Result:
    attempts = 0
    broken_items_amount = 0
    step = get_optimal_step(starting_floor, ending_floor)
    curr_floor = starting_floor + step - 1

    # DEBUG
    logger.debug(f'setup\n'
                 f'\tstarting floor: {curr_floor}\n'
                 f'\tending floor: {ending_floor}\n'
                 f'\tbreaking floor: {breaking_floor}\n'
                 f'\toptimal starting step: {step}')

    while curr_floor <= ending_floor:
        # DEBUG
        logger.debug(f'find first time the item breaks\n'
                     f'\tattempt number: {attempts + 1}\n'
                     f'\tcurrent floor: {curr_floor}\n'
                     f'\tstep size: {step + 1}')

        attempts += 1
        if throw_ball(curr_floor, breaking_floor):
            broken_items_amount += 1
            break

        step -= 1
        curr_floor += step

    # Round the floor according to the floor limit
    curr_floor = min(curr_floor, ending_floor)

    for floor in range(curr_floor - step, curr_floor + 1):
        # DEBUG
        logger.debug(f'go up until the item breaks again\n'
                     f'\tattempt number: {attempts + 1}\n'
                     f'\tcurrent floor: {floor}\n'
                     f'\tstep size: 1')

        attempts += 1
        if throw_ball(floor, breaking_floor):
            broken_items_amount += 1

            # DEBUG
            logger.debug(f'result\n'
                         f'\tattempts: {attempts}\n'
                         f'\tbroken items amount: {broken_items_amount}\n'
                         f'\tbreaking floor guessed: {ending_floor}\n'
                         f'\n--------------------------\n')

            return Result(attempts, broken_items_amount, floor)

    logger.warning('No breaking floor found in the given range')
    return Result(attempts, broken_items_amount, ending_floor)