# Library Management API

This project provides a RESTful API for managing a library system. It's built with FastAPI and uses SQLAlchemy for database interactions. The API allows for operations on books and authors, including creating, listing, updating, and deleting entries.



## Features

- CRUD operations for books and authors
- Search functionality for books and authors
- Association of books with authors


## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- poetry 
  

## If  you what to init the project for the first time you can run the folloing commend : 

```
make init 
```


## Setup & Installation

Ensure you have Python 3.7 or higher installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).

This project uses [Poetry](https://python-poetry.org/docs/) for managing dependencies. To get started with Poetry, install it using the official instructions provided in the Poetry documentation.

Once Poetry is installed, navigate to the project's root directory and run the following command to install dependencies and set up the project's virtual environment:



```shell
poetry install --no-root

```

## Running the Application
### Activate the virtual environment managed by Poetry: 
```shell
poetry shell
```
### Then start the FastAPI server with:

```
uvicorn main:app --reload
```

or use the Makefile:
```
make run 
```