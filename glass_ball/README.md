1. as fast as possible (minimal attempts)
2. as minimal broken glass balls as possible


### binary search

### optimal steps
x + (x-1) + (x-2) + (x-3) + ... + 1 = number of floors
(x*(X+1) // 2) = number of floors


current floor status      | momentum (went up or down from last floor to curr) | broke last floor == Flase | broke last floor == True | 
--------------------------|----------------------------------------------------|---------------------------|--------------------------| 
broke curr floor == False | momentum == up                                     | X cant be                 | X cant be                |
broke curr floor == False | momentum == down                                   | go down                   | go up in smaller steps   |
broke curr floor == True  | momentum == up                                     | go down in smaller steps  | X cant be                |
broke curr floor == True  | momentum == down                                   | X cant be                 | go up                    |

