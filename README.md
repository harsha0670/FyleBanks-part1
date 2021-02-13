# Banks - REST Api

A Django App that is a REST service which can fetch bank details, using the data given in the API’s query parameters.
The app uses powerful Django rest-framework to create APIs.

Endpoint 1: /api/branches/autocomplete?search="**_query_**"

  Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
  
  Eg: /api/branches/autocomplete?search=**RTGS**&limit=3&offset=0
  
Endpoint 1: /api/branches/branches?search="**_query_**"

Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.

  Eg: /api/branches/branches?search=**Bangalore**&limit=3&offset=0
  
## Hosted URLs

**Url 1** https://desolate-meadow-48761.herokuapp.com/api/autocomplete

**Url 2** https://desolate-meadow-48761.herokuapp.com/api/branches



## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
