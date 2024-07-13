from random import randrange
import matplotlib.pyplot as plt

import binary_search
import optimal_steps
import optimal_steps_with_binary_search

MIN_STARTING_FLOOR = 1
MAX_ENDING_FLOOR = 200

def main() -> None:
    starting_floor = randrange(MIN_STARTING_FLOOR, MAX_ENDING_FLOOR)
    ending_floor = randrange(starting_floor, MAX_ENDING_FLOOR + 1)
    # DEBUG
    starting_floor = 1
    ending_floor = 100
    # starting_floor = 60
    # ending_floor = 80
    breaking_floor = randrange(starting_floor, ending_floor + 1)

    binary_search_attempts = []
    binary_search_broken_balls = []
    binary_search_accuracy = []
    optimal_steps_attempts = []
    optimal_steps_broken_balls = []
    optimal_steps_accuracy = []
    optimal_steps_with_binary_search_attempts = []
    optimal_steps_with_binary_search_broken_balls = []
    optimal_steps_with_binary_search_accuracy = []
    breaking_floors_list = range(starting_floor, ending_floor + 1)

    for curr_breaking_floor in breaking_floors_list:
        binary_search_result = binary_search.find_breaking_floor(starting_floor, ending_floor, curr_breaking_floor)
        optimal_steps_result = optimal_steps.find_breaking_floor(starting_floor, ending_floor, curr_breaking_floor)
        optimal_steps_with_binary_search_result = optimal_steps_with_binary_search.find_breaking_floor(starting_floor, ending_floor, curr_breaking_floor)

        binary_search_attempts.append(binary_search_result[0])
        binary_search_broken_balls.append(binary_search_result[1])
        binary_search_accuracy.append(100 if (binary_search_result[2] == curr_breaking_floor) else 0)
        optimal_steps_attempts.append(optimal_steps_result[0])
        optimal_steps_broken_balls.append(optimal_steps_result[1])
        optimal_steps_accuracy.append(100 if (optimal_steps_result[2] == curr_breaking_floor) else 0)
        optimal_steps_with_binary_search_attempts.append(optimal_steps_with_binary_search_result[0])
        optimal_steps_with_binary_search_broken_balls.append(optimal_steps_with_binary_search_result[1])
        optimal_steps_with_binary_search_accuracy.append(100 if (optimal_steps_with_binary_search_result[2] == curr_breaking_floor) else 0)

    # Plotting the results
    plt.figure(figsize=(21, 6))

    # Plot attempts
    plt.subplot(1, 3, 1)
    plt.plot(breaking_floors_list, optimal_steps_attempts, label='Two-Ball Algorithm')
    plt.plot(breaking_floors_list, binary_search_attempts, label='Binary Search Algorithm')
    plt.plot(breaking_floors_list, optimal_steps_with_binary_search_attempts, label='Combination Algorithm')
    plt.xlabel('Breaking Floor')
    plt.ylabel('Number of Attempts')
    plt.title('Number of Attempts Comparison')
    plt.legend()

    # Plot broken balls
    plt.subplot(1, 3, 2)
    plt.plot(breaking_floors_list, optimal_steps_broken_balls, label='Two-Ball Algorithm')
    plt.plot(breaking_floors_list, binary_search_broken_balls, label='Binary Search Algorithm')
    plt.plot(breaking_floors_list, optimal_steps_with_binary_search_broken_balls, label='Combination Algorithm')
    plt.xlabel('Breaking Floor')
    plt.ylabel('Number of Broken Balls')
    plt.title('Number of Broken Balls Comparison')
    plt.legend()

    # Plot accuracy
    plt.subplot(1, 3, 3)
    plt.plot(breaking_floors_list, optimal_steps_accuracy, label='Two-Ball Algorithm')
    plt.plot(breaking_floors_list, binary_search_accuracy, label='Binary Search Algorithm')
    plt.plot(breaking_floors_list, optimal_steps_with_binary_search_accuracy, label='Combination Algorithm')
    plt.xlabel('Breaking Floor')
    plt.ylabel('Accuracy (%)')
    plt.title('Accuracy Comparison')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # # DEBUG
    # print("SETUP\n"
    #       "~~~~~\n"
    #       f"starting floor: \t{starting_floor}  \n"
    #       f"ending floor:   \t{ending_floor}    \n"
    #       f"breaking floor: \t{breaking_floor}  \n\n")
    #
    # print("binary tree:")
    # attempts, glass_balls_broken, suggested_floor = binary_search.find_breaking_floor(starting_floor, ending_floor, breaking_floor)
    #
    # # print("optimal steps:")
    # # attempts, glass_balls_broken, suggested_floor = optimal_steps.find_breaking_floor(starting_floor, ending_floor, breaking_floor)
    #
    # # print("optimal step + binary tree:")
    # # optimal_steps_with_binary_search.find_breaking_floor(starting_floor, ending_floor, breaking_floor)
    #
    # # DEBUG
    # print(f"\n\nANSWER\n"
    #       f"num of attempts: {attempts}\n"
    #       f"num of broken glass balls: {glass_balls_broken}\n"
    #       f"I think the breaking floor is {suggested_floor}")


if __name__ == '__main__':
    main()