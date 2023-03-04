# Setup

## Requirements

Python 3.10 or higher is required. 

This is not a tutorial for python, but if you don't have it installed, you can get it from [python.org](https://www.python.org/).

## Installation

1. Clone the repository

2. Create a virtual environment with `python -m venv venv`

|⚠️ Note: Replace python with your alias for your installation of python|

3. Activate the virtual environment with `. ./venv/bin/activate` for linux or `./venv/Scripts/activate` on Windows

4. Install the requirements with `pip install -r requirements.txt`

5. You're done! (the test files should not be run with python, instead they should be run with `pytest`)

## Pushing

1. Run `black .` to format the code

2. Run `pytest` to make sure the tests pass

3. Commit and push
