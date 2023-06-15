# Phase 4, Lecture 4: Constraints and Validations

## Lecture Topics

- Constraints
- Validations
- SerializerMixin

## Introduction

In today's lecture, we will talk about Constraints, Validations, and SerializerMixin.

## Setup

1. Fork and then Clone this repository.

2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required libraries.

3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

4. Enter the command `cd server` in the terminal to move into the server directory.

5. Run these commands in the terminal (make sure that you are in the `server` directory before running these terminal commands):

```py
export FLASK_APP=app.py

export FLASK_RUN_PORT=7000
```

6. We will write code in the `models.py` file to implement constraints, validations, and SerializerMixin.

7. Enter the command `flask run` or `python app.py` in the terminal to run the Flask app (make sure that you are in the `server` directory before running these terminal commands).

- Note: You can enter the command `flask run --debug` which is another option to run the flask app with debug mode on.