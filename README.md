# late-show-challenge
A Flask-based RESTful API for managing episodes, guests, and their appearances on a talk show. Built for Phase 4 of the Software Engineering curriculum.

## Features
View all episodes
View episode details with guest appearances
View all guests
Create a new appearance for a guest on an episode
Validates ratings and relationships
Uses SQLAlchemy ORM with Flask-Migrate
JSON serialization with custom serialization rules

## Technologies
Python 
Flask
Flask-RESTful
Flask-CORS
Flask-Migrate
SQLAlchemy
SQLite 

## Project Structure
lateshow-stacy-waithera/
├── server/
│   ├── app.py            
│   ├── models.py          
│   ├── config.py          
│   ├── seed.py            
│   └── migrations/      
├── README.md
├── requirements.txt
└── instance/
    └── app.db             

## Setup Instructions
Clone the repo
git clone git@github.com:Waith93/lateshow-stacy-waithera.git

cd lateshow-stacy-waithera

## Create a virtual environment
 pipenv shell

## Install dependencies
pipenv install

## Run migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## Seed the database
python server/seed.py

## Start the server
flask run

## API Endpoints
GET /episodes
Returns all episodes:

GET /episodes/<int:id>
Returns episode with guests:

GET /guests
Returns all guests.

POST /appearances
Create a new appearance:

## Validations
rating must be between 1 and 5

guest_id and episode_id must exist in the database

## Author
Stacy Waithera