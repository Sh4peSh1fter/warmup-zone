def print_chess_board(length: int, width: int) -> None:
    # input validation - is int
    if not isinstance(length, int) or not isinstance(width, int):
        raise ValueError("length and width must be integers.")
    # input validation - greater than 0
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be positive integers (greater than 0).")

    print(f"{length}x{width} chess board:\n"
          f"-----------------")
    for l_index in range(1, length + 1):
        for w_index in range(1, width + 1):
            # DEBUG
            # print(f"length: {l_index}, width: {w_index}, modulo: {(l_index + w_index) % 2}")
            if (l_index + w_index) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("\n", end="")
    print("\n", end="")

def main():
    print_chess_board(6, 3)
    print_chess_board(8, 8)


if __name__ == '__main__':
    main()