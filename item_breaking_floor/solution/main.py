# imports
from random import randrange
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from config import configure_logging
from config import MIN_STARTING_FLOOR, MAX_ENDING_FLOOR, ALGORITHMS_IN_USE, DEBUG
from config import Result
## custom modules
import binary_search
import optimal_steps


# logging
configure_logging(DEBUG)


def generate_results(algorithm, start: int, end: int, floors: List[int]) -> List[Result]:
    return [algorithm.find_breaking_floor(start, end, floor) for floor in floors]


def plot_results(breaking_floors: List[int], results: List[List[Result]]):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(21, 6))

    for res, label in zip(results, ALGORITHMS_IN_USE):
        attempts = [r.attempts for r in res]
        broken_items_amount = [r.broken_items_amount for r in res]
        accuracy = [100 if r.breaking_floor == f else 0 for r, f in zip(res, breaking_floors)]

        ax1.plot(breaking_floors, attempts, label=label)
        ax2.plot(breaking_floors, broken_items_amount, label=label)
        ax3.plot(breaking_floors, accuracy, label=label)

    ax1.set(xlabel='Breaking Floor', ylabel='Number of Attempts', title='Number of Attempts Comparison')
    ax2.set(xlabel='Breaking Floor', ylabel='Number of Broken Items', title='Number of Broken Items Comparison')
    ax3.set(xlabel='Breaking Floor', ylabel='Accuracy (%)', title='Accuracy Comparison')

    for ax in (ax1, ax2, ax3):
        ax.legend()

    plt.tight_layout()
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()


def main() -> None:
    starting_floor = randrange(MIN_STARTING_FLOOR, MAX_ENDING_FLOOR)
    ending_floor = randrange(starting_floor, MAX_ENDING_FLOOR + 1)
    # DEBUG
    # starting_floor = 1
    # ending_floor = 100
    # starting_floor = 60
    # ending_floor = 80
    breaking_floors = list(range(starting_floor, ending_floor + 1))

    algorithms = [binary_search, optimal_steps]
    results = [generate_results(alg, starting_floor, ending_floor, breaking_floors) for alg in algorithms]

    plot_results(breaking_floors, results)


if __name__ == '__main__':
    main()