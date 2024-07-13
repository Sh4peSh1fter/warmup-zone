def bottom_up(num_index: int) -> int:
    if num_index == 1 or num_index == 2:
        return 1

    fibonacci_list = [1] * num_index

    for i in range(2, num_index):
        fibonacci_list[i] = fibonacci_list[i - 1] + fibonacci_list[i - 2]

    return fibonacci_list[num_index - 1]


def recursive_memoization(num_index: int, memo={}) -> int:
    if num_index == 1 or num_index == 2:
        return 1
    if num_index not in memo:
        memo[num_index] = recursive_memoization(num_index - 1, memo) + recursive_memoization(num_index - 2, memo)
    return memo[num_index]


def main():
    print(bottom_up(2))
    print(bottom_up(33))
    print(bottom_up(58))

    print(recursive_memoization(2))
    print(recursive_memoization(33))
    print(recursive_memoization(58))


if __name__ == '__main__':
    main()