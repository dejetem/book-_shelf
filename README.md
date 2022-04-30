## Getting Started the first thing to do is to clone the repository:

```bash
$ git clone https://github.com/dejetem/book-_shelf.git
$ cd book-_shelf
```

## Create a virtual environment to install dependencies in and activate it:

```bash
$ python -m venv env
$ env\Scripts\activate.bat
$ cd book
```

## Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by venv

## run the server:

```bash
(env)$ python manage.py runserver
```
Open your a tab on your browser and input this url 
## http://127.0.0.1:8000/ 
it will open a swagger-ui contain the documentation for the all the endpoints


