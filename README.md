# ORIGIN #
This project is an exercise done as part of an OpenClassrooms training course for developers in the Python language.
It corresponds to project 11 of the training.

# GOAL OF THE PROJECT 11 #
Project 11 aims to improve an existing project, in this case project 10, by fixing a bug and creating a new feature.

# GOAL OF THE APPLICATION #
This application makes it possible to choose a food for which one wishes to obtain a better quality substitute, in order to improve one's diet. It's based on the Open Food Facts database. Open Food Facts is a free and collaborative database referencing food products from all over the world.

The Open Food Facts website (FR): https://fr.openfoodfacts.org/

To see the full Readme of the project 10 : https://github.com/Githb-usr/purbeurre-deployment

# GUIDELINES #
* The source code is on Github and has a consistent commit history.
* The new functionality includes unit and functional tests.
* Code written entirely in English: functions, variables, comments, etc.
* Use an agile project methodology to work in project mode.

# DEPLOYMENT #
* PostGreSQL must be installed on the server, with "unaccent" extension.
* Create a "purbeurre" database and a user with password
* Creating a virtual environment with Python 3.8
* Clone the application
* Run the following command to install the necessary libraries :
  - pip install -r requirements.txt
* Create an .env file with these environment variables (replace the xxx with your values):
  - DJANGO_SETTINGS_MODULE=config.settings
  - SECRET_KEY=xxx
  - DB_NAME=xxx
  - DB_USER=xxx
  - DB_PASSWORD=xxx
  - DB_HOST=xxx
  - DB_PORT=xxx
* Generate the static files:
  - [python3] manage.py collectstatic
* Create the database tables:
  - [python3] manage.py migrate
* Populating the database:
  - [python3] manage.py import_data
* Run the application locally
  - [python3] manage.py runserver
* Run the tests
  - [python3] manage.py test tests