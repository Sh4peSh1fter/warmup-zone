# print chess board
difficulty - easy (1)

## mission
write a function that prints a chess board pattern with the given length and width.
black is represented by '0' and white by '1'.

for example:
```python
print_chess_board(length=6, width=3)

# output
"""
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
"""
```

notes:
1. "length" represent columns, "width" represents rows.
2. the chess board always starts from "1" in the top left corner.
3. no square is adjacent to the same color as himself, except of its corners - just like a chess board.
