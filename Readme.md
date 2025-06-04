
### Animal Crossing Collectable Tracker ###

# Setup

1. Clone the public repository:
https://github.com/MelahatTur/animalcrossing.git

2. create and activate a virtual environment
Windows:
    python -m venv .venv
    Set-ExecutionPolicy Unrestricted -Scope Process
    .venv\Scripts\activate

macOS/Linux:
    python3 -m venv .venv
    . .venv/bin/activate

3. Install required packages using requirements.txt
pip install -r requirements.txt

4. Open Docker Desktop and activate
If you have another docker container open, you need to close it with:
    docker-compose up -d

You'll then have to build the docker container:
    docker compose up --build -d

5. Open the webapp from your browser:
Insert following link:
    http://localhost:5000/

# Navigation through the webapp
You can navigate through the webapp's pages using the buttons appearing or following the links to the pages:
- Home (http://localhost:5000/)                 : The initial page, where you can register or login
    - Register (http://localhost:5000/register) : Where you can register an account
    - Login (http://localhost:5000/login)       : Where you can log in on your account.
- Dashboard (http://localhost:5000/dashboard    : If you're logged in, you enter your dashboard.
            or http://localhost:5000/login)       If you're not logged in, you'll go to login page.
- Logout                                        : Not a page, but a function which logs you out of your account and deletes it.

# Folder content


