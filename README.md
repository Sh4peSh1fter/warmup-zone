# usful commands
### create a new project and setup virtual environment and poetry
```commandline
cd <project_folder>
echo "# README" > README.md
mkdir solution
cd solution
echo "# README" > README.md

python -m venv .venv

.\.venv\Scripts\Activate.ps1    # for windows

pip install poetry

poetry init
```
### start working on a project
optional steps before running the project
```commandline
cd <project_folder>/solution/

.\.venv\Scripts\Activate.ps1

# add modules if needed
poetry add <module_name>
```
run the project
```commandline
# install modules if not installed in venv yet
poetry install

poetry run <file_name>
```
finish working on a project
```commandline
deactivate

cd ../../
# the current path should be "warmup-zone"

git status
...
```


# python best practices and conventions
1. when declaring variables, define their types.
```python
def main():
    var1: int = 5
    var2: str = ""
```
2. when declaring a function, define the types of the given variables, and the expected return type of the function itself.
```python
def func(var1: int, var2: str) -> bool:
    return True
```
3. import only the functions you need from a module. make sure the function you import has a unique name, as it can be mixed by mistake with other functions that has the same name.
```python
from time import timezone
# instead of: import time 

timezone()
# instead of time.timezone()
```
4. there is no difference between single quotes and double quotes, so just stick to one of them for consistency in your code. 
I prefer to use single quotes in default.
```python
# default
print('yo')
# string inside a string
my_str = 'he said: "yo"'
# apostrophes
apostrophes = 'you\'re great'
# function documentation
def func():
    """ this function does nothing """
    pass
```
