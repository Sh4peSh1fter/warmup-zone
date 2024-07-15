1. as fast as possible (minimal attempts)
2. as minimal broken glass balls as possible


you are given a material that breaks on a certain height 
now you are given a material that explodes from a certain height

material breaking floor

material -> object?

### binary search

### optimal steps
The sum of these steps should cover the entire range of floors:
x + (x-1) + (x-2) + ... + 1 = floor_range
This sum can be written as: x + (x-1) + (x-2) + ... + 1 = x(x+1)/2
So, we have the equation:
x(x+1)/2 = floor_range
Solving this quadratic equation:
x^2 + x - 2floor_range = 0
Using the quadratic formula, we get:
x = (-1 + sqrt(1 + 8floor_range)) / 2
Since we need an integer step size, we use the ceiling function:
x = ceil((-1 + sqrt(1 + 8*floor_range)) / 2)

This formula gives us the smallest integer x such that x(x+1)/2 is greater than or equal to floor_range. This ensures that our steps will cover the entire range of floors while minimizing the worst-case number of drops.


current floor status      | momentum (went up or down from last floor to curr) | broke last floor == Flase | broke last floor == True | 
--------------------------|----------------------------------------------------|---------------------------|--------------------------| 
broke curr floor == False | momentum == up                                     | X cant be                 | X cant be                |
broke curr floor == False | momentum == down                                   | go down                   | go up in smaller steps   |
broke curr floor == True  | momentum == up                                     | go down in smaller steps  | X cant be                |
broke curr floor == True  | momentum == down                                   | X cant be                 | go up                    |

