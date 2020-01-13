# QCTRL Backend Challenge Project

This Django project is created as part of the backend engineering challenge posted by Q-CTRL. The challenge can be accessed from https://github.com/qctrl/back-end-challenge/tree/4789debc2c9f904dc486711ccf1b470903376900

## Table of Contents

- [Requirements](#Requirements)
- [Usage](#Usage)
- [Assumptions](#Assumptions)
- [API](#API)
- [Alternative Installation](#alternative-installation)


## Requirements
This project needs to following:

* docker (tested on 18.09)
* docker-compose (1.17)

The project heavily depends on docker to make it easy to test and run the project, and provides an simple point of entry for QCTRL members that will evaluate this project

## Usage 
In root directly of the repository, run the following command

`
docker-compose up
`

This will run:
- Django app on localhost:8000
- Postresql on localhost:15432
- PgAdmin on localhost:15050

You can run the following to run docker-compose in deattached mode

`
docker-compose up -d
`

#### Configurations
In case default configurations are not desired, create a '.env' file in root folder and change environment variables to your need. The following table shows all expected needed configurations with default values:

| Configuration | Default Value |
|-------------- |---------------|
| APP_HOST      | 0.0.0.0       |
| APP_PORT      | 8000          |
| DB_NAME       | app           |
| DB_USER       | postgres      |
| DB_PASS       | password      |

#### Using PgAdmin
PgAdmin can be reached from http://localhost:15050. Use the following Credentials
* **user**: admin@pgadmin.org
* **password**: password

#### Running Test
Make sure the docker-compose service are down, then run the command

`
docker-compose run app sh -c "python manage.py test"
`

This will run all unit tests written for the project


#### Further development
The docker-compose file is configured for the app image to have an attached volume linked to the app folder. This allows hot changes to be dynamically updated after each save.

Because all requirements are within the docker image, there is no need to install any other requirements for development. In case a new library is needed, add it to the **Pipfile** inside the app folder. Then rebuild the image

`
docker-compose build
`

# Assumptions
There are some simple things that I assumed when creating the Control Model. These are:
- Name will not exceed 255 character
- type is case sensitive
- maximum_rabi_rate and polar_angle have **5** decimal places

# APIs
The following serves as the seven required services in the challenge:

| Service           | Path                 | Method  |
|-------------------|----------------------|---------|
| Create            | api/control          | POST    |
| List              | api/control          | GET     |
| Retrieve specific | api/control/{id}     | GET     |
| Update specific   | api/control/{id}     | PUT     |
| Delete specific   | api/control/{id}     | DELETE  |
| Bulk Create       | api/control/upload   | POST    |
| Download CSV      | api/control/download | GET     |


# Alternative Installation
The previous approach of having all requirements within docker helps to ease sharing development environment within a team, but it also comes with its disadvantages. If using an IDE, not having a python environment with all requirements would mean the IDE will not be able to function as its meant to be. 

This section provides an alternative approach, explaining project requirements and and to run the application on local host without docker.

### Requirements:
* Python 3.7
* Python-virtualenv
* Pip
* psyocpg2
* Postgresql

`
Note: Do not use psyocpg2 binary distribution as it might cause problem when migrating database. Installing psycopg2 from source is a bit challenging, but all requirements are explained on the library's website
`

### Inital Setup:

- Create a python virtual environment
`
python3.7 -m venv venv
`

- Activate environment
`
source venv/bin/activate
`
- Install pipenv
`
pip install pipenv
`
- Install dependencies
`
pipenv install`

`Note: Make sure you have all psyocpg2 requirements met at this point, or installation would fail. If it fails, provide requiements then run the command again`


At this stage, the application is ready. All that is needed is to migrate database. Before doing that, make sure you have postgresql database server running. You will need to change the default connection settings found inside **app/qctrl/settings.py** to match your needs.

- Migrate database changes:
`
python manage.py migrate
`

### Testing and Running the Server

To test, run the following command
`
python manage.py test
`

To run the server in localhost:8000
`
python manage.py runserver localhost:8000