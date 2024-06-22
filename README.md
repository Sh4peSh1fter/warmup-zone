# usful commands
### create a new project and setup virtual environment and poetry
```commandline
cd <project_folder>

python -m venv .venv

.\.venv\Scripts\Activate.ps1    # for windows

pip install poetry

poetry init
```
### start working on a project
optional steps before running the project
```commandline
cd <project_folder>

.\.venv\Scripts\Activate.ps1

# install modules if needed
poetry add <module_name>
```
run the project
```commandline
poetry run <file_name>
```
finish working on a project
```commandline
deactivate

cd ..
```


# python best practices
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
