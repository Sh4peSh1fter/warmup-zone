# Imports
from logging_config import setup_module_logger

# Consts
STARTING_ATTEMPTS = 0
STARTING_BROKEN_BALLS = 0

# Logging
logger = setup_module_logger(__name__)

def throw_ball(curr_floor: int, breaking_floor: int) -> bool:
    # DEBUG
    logger.debug(f'throw and check if the ball breaks\n'
                 f'\twill the ball break? {curr_floor >= breaking_floor}')

    return curr_floor >= breaking_floor

def recursive_binary_search(low, high, breaking_floor, attempts, broken_balls):
    if low == high:
        return attempts, broken_balls, low

    mid = (low + high) // 2

    attempts += 1
    if throw_ball(mid, breaking_floor):
        broken_balls += 1
        return recursive_binary_search(low, mid, breaking_floor, attempts, broken_balls)
    else:
        return recursive_binary_search(mid + 1, high, breaking_floor, attempts, broken_balls)

def binary_search(low, high, breaking_floor, attempts, broken_balls):
    last_safe_floor = 0

    while low <= high:
        mid = (low + high) // 2

        # DEBUG
        logger.debug(f'debug values\n'
                     f'\tattempt number: {attempts + 1}\n'
                     f'\tcurrent floor: {mid}')

        attempts += 1
        if throw_ball(mid, breaking_floor):
            broken_balls += 1
            high = mid - 1
        else:
            last_safe_floor = mid
            low = mid + 1

    # DEBUG
    logger.debug(f'result\n'
                 f'\tattempts: {attempts}\n'
                 f'\tbroken balls: {broken_balls}\n'
                 f'\tbreaking floor guessed: {last_safe_floor + 1}\n'
                 f'\n--------------------------\n')

    return attempts, broken_balls, last_safe_floor + 1


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int):
    # DEBUG
    logger.debug(f'setup\n'
                 f'\tstarting floor: {starting_floor}\n'
                 f'\tending floor: {ending_floor}\n'
                 f'\tbreaking floor: {breaking_floor + 1}')

    # return recursive_binary_search(starting_floor, ending_floor, breaking_floor, STARTING_ATTEMPTS, STARTING_BROKEN_BALLS)
    return binary_search(starting_floor, ending_floor, breaking_floor, STARTING_ATTEMPTS, STARTING_BROKEN_BALLS)