
# Animal Crossing Collectable Tracker
This web application was developed as a group project for the Databases and Information Systems course at the University of Copenhagen.
The Animal Crossing Collectable Tracker is designed for players of Animal Crossing: New Horizons, allowing users to create an account and explore a structured collection of critters from the game. Once the user has registered an account, users can search and filter through various categories of collectables to view detailed information.
In addition to browsing, users can add items to their personal collection, which is then displayed on their dashboard for tracking progress and planning future in-game collecting.
The app combines PostgreSQL, Flask, and CSV-based data import to deliver a functional companion tool for Animal Crossing fans.

## Setup

1. Clone the public repository:
```shell
https://github.com/MelahatTur/animalcrossing.git
```

2. create and activate a virtual environment:
Windows:
```shell
python -m venv .venv
Set-ExecutionPolicy Unrestricted -Scope Process
.venv\Scripts\activate
```

macOS/Linux:
```shell
python3 -m venv .venv
. .venv/bin/activate
```

3. Open Docker Desktop and activate
If you have another docker container open, you need to close it with:
```shell
docker-compose down
```

You'll then have to build the docker container:
```shell
docker compose up --build -d
```

4. Open the webapp from your browser:
```shell
http://localhost:5000/
```
## Navigation through the webapp
You can navigate through the webapp's pages using the buttons appearing or following the links to the pages:

|Command                |Link to page                      |Description                                                   |
|-----------------------|----------------------------------|--------------------------------------------------------------| 
|Home                   |http://localhost:5000/            |The initial page, where you can register or login             |
|Register               |http://localhost:5000/register    |Where you can register an account                             |
|Login                  |http://localhost:5000/login       |Where you can log in on your account.                         |
|Dashboard              |http://localhost:5000/dashboard   |If you're logged in, you enter your dashboard. Here you can view your collection and your progress. You can also delete your account.                |
|Collectables           |http://localhost:5000/collectables| Where you can search and filter through collectables. if you're logged in, you can also add the an collectable to your dashboard.                |
|Logout                 |                                  |Not a page, but a function which logs you out of your account.|

## Folder content
We have followed the Model View Controller pattern to organize our web application, though we call View for templates. The implementation of the app is implemented in the folder __animalcros__. Here is a preview and explanation of the folders the __animalcros__ folder contains:
- __controllers__ : Links model and templates. Holds logic for different URL routes.
- __data__ : Contains .csv data files and images for each collectable.
- __models__: The internal representation of the information, here we interact with the database.
- __static__ \ __css__: Common styling for the entire webapp
-__templates__: HTML templates for each page. The interface for the user.
-__utils__: initializes the database, importing data from .csv and defining SQL schema.

Here is the files in the __animalcros__ folder:
- __\_\_init\_\_.py__: Initializes the flask-applikation, set up the database, loads data, and registers all blueprints for routing.
- __forms.py__: Defines Flask-WTF forms for user registration and login, including input fields and validation rules.

Here is the files in the general __animalcrossing__ folder:
- __.gitattributes__: Git configuration files for ignoring temp or config files.
- __app.py__: The main entry point for the Flask application. Initializes and runs the app.
- __docker-compose.yaml__: Defines Docker services.
- __Dockerfile__: Instructions for bulding the Docker image for the Flask app.
- __entrypoint.sh__: Shell script that runs on Docker container startup.
- __pyproject.toml__: Used to define the project metadata and dependencies.
- __Readme.md__: This file. Documentation for setting up and using the project.
