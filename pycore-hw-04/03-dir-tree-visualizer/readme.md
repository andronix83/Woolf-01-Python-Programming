# Installation Manual

Since this is not recommended to check into VCS virtual environments,
here I provide the instruction on how to locally install and activate
Virtual Environment (venv) with the proper dependencies.

## Create and activate Virtual Environment
- Open the Terminal and switch to the directory, where this file is located
- Run `python -m venv .venv` command to initialize venv
- Run `.\.venv\Scripts\activate` command to activate venv

## Install the required dependencies
- Run`pip install -r requirements.txt` command to install dependencies into venv
- After this you can run the script

## Project modification
- If you added any new dependencies or updated the existing ones,
please update the `requirements.txt` file accordingly
- Run `pip freeze > requirements.txt` command for this

## Deactivation
- Run `deactivate` command to deactivate venv