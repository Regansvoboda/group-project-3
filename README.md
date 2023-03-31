Introduction
This is a simple CLI app written in Python that connects to a SQLite database. The app has four tables - Patient, Doctor, Unit, and Visit. It uses SQLAlchemy and Alembic for database management. The app allows the user to list out patients, doctors, units, and visits.

Installation
To install the app, clone this repository to your local machine. You will need Python 3.6 or above and pip installed on your machine.

Once you have cloned the repository, navigate to the project directory and run the following command to install the necessary packages:

Copy code
pip install -r requirements.txt
Database setup
The app uses SQLite as its database. The database is already created and is located in the database directory. If you want to create a new database, you can do so by running the following command:

Copy code
python models.py
This will create a new database in the database directory.

Seed data
The app comes with seed data that you can use to populate the database. To seed the database, run the following command:

Copy code
python seed.py
Usage
To use the app, navigate to the project directory and run the following command:

Copy code
python cli.py
This will start the app and show you a menu. From the menu, you can choose to list out patients, doctors, units, or visits.