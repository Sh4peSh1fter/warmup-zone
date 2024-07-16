# Item Breaking Floor - Solution
we have 2 questions, each has its own unique approach and algorithm to solve it.

### find breaking floor with the least amount of tries
a simple binary search should do the trick.

### find breaking floor with the least amount of broken items
this is a more interesting problem which requires a different approach.
we want to move in optimal steps across the floors, without wasting time or breaking the item if its not necessary.

instead of jumping in steps of 1 in a linear search from bottom to top (to avoid the item breaking), 
we will jump in sections, and use the first item to eliminate them quickly until it breaks.
then we just drop the items from the last section we stopped on.

to optimize it and find the size of sections we are jumping, we will need some math.
the sum of the optimal steps should cover the entire range of floors:

x + (x-1) + (x-2) + ... + 1 = floor_range

this sum can be written as: 

x + (x-1) + (x-2) + ... + 1 = x * (x+1) / 2

so, we have the equation:

x * (x+1) / 2 = floor_range

solving this quadratic equation:

x^2 + x - 2 * floor_range = 0

using the quadratic formula, we get:

x = (-1 + sqrt(1 + 8 * floor_range)) / 2

this formula gives us the smallest integer x such that x* (x+1) / 2 is greater than or equal to floor_range. this ensures that our steps will cover the entire range of floors while minimizing the worst-case number of drops.


## Folder Structure
```commandline
solution
├── .venv/              # python virtual environment
├── logs/               # logs folder
├── main.py             # run the algorithms and show graph 
├── config.py           # contain configuration related values and functions
├── binary_search.py    # binary serach solution
├── optimal_steps.py    # 2 ball solution
├── pyproject.toml      # poetry file
└── README.md
```

## Getting Started
1. make sure you are in the correct path (".../item_breaking_floor/solution/"):
```commandline
cd <project_solution_folder>
```
2. create a virtual environment to work with, and install poetry and other modules and dependencies:
```commandline
python -m venv .venv

.\.venv\Scripts\Activate.ps1    # for windows

pip install poetry

poetry install
```
3. run the project:
```commandline
# with poetry
poetry run main.py

# or

# with python
python main.py
```
4. if you want to output logs, replace the value of "DEBUG" in the config.py file to "True", and run the project again.
    logs are outputted into the "logs" folder, each algorithm has its own log file.

# Usage
you can add new algorithms easily and compare them to the others in a simple graph.
to do so, adjust the config.py and main.py files.

# To do
1. maybe it will be cool if we write one function that also gets the number of items and determines which algorithm should we use.
2. make the optimal steps algorithm to optimize according to given number of items.