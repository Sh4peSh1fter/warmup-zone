# Imports
from config import setup_module_logger
from config import STARTING_ATTEMPTS, STARTING_BROKEN_ITEMS_AMOUNT, Result


# Logging
logger = setup_module_logger(__name__)


def throw_item(curr_floor: int, breaking_floor: int) -> bool:
    # DEBUG
    logger.debug(f'throw and check if the item breaks\n'
                 f'\twill the item break? {curr_floor >= breaking_floor}')

    return curr_floor >= breaking_floor

def recursive_binary_search(low: int, high: int, breaking_floor: int, attempts: int, broken_items_amount: int) -> Result:
    if low == high:
        return Result(attempts, broken_items_amount, low)

    mid = (low + high) // 2

    attempts += 1
    if throw_item(mid, breaking_floor):
        broken_items_amount += 1
        return recursive_binary_search(low, mid, breaking_floor, attempts, broken_items_amount)
    else:
        return recursive_binary_search(mid + 1, high, breaking_floor, attempts, broken_items_amount)

def binary_search(low: int, high: int, breaking_floor: int, attempts: int, broken_items_amount: int) -> Result:
    last_safe_floor = low - 1

    while low <= high:
        mid = (low + high) // 2

        # DEBUG
        logger.debug(f'debug values\n'
                     f'\tattempt number: {attempts + 1}\n'
                     f'\tcurrent floor: {mid}')

        attempts += 1
        if throw_item(mid, breaking_floor):
            broken_items_amount += 1
            high = mid - 1
        else:
            last_safe_floor = mid
            low = mid + 1

    # DEBUG
    logger.debug(f'result\n'
                 f'\tattempts: {attempts}\n'
                 f'\tbroken items amount: {broken_items_amount}\n'
                 f'\tbreaking floor guessed: {last_safe_floor + 1}\n'
                 f'\n--------------------------\n')

    return Result(attempts, broken_items_amount, last_safe_floor + 1)


def find_breaking_floor(starting_floor: int, ending_floor: int, breaking_floor: int):
    # DEBUG
    logger.debug(f'setup\n'
                 f'\tstarting floor: {starting_floor}\n'
                 f'\tending floor: {ending_floor}\n'
                 f'\tbreaking floor: {breaking_floor}')

    # return recursive_binary_search(starting_floor, ending_floor, breaking_floor, STARTING_ATTEMPTS, STARTING_broken_items_amount)
    return binary_search(starting_floor, ending_floor, breaking_floor, STARTING_ATTEMPTS, STARTING_BROKEN_ITEMS_AMOUNT)