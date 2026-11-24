Table Of Contents:
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Starting](#starting-the-application)
    - [With Docker](#docker)
    - [With Commands](#commands)
        - [Frontend](#frontend)
        - [Server](#backend)
        
# Introduction

This is the repo for the game WordHoarder, in which players enter words that fit the criteria for the day, gaining points from the number of words they have, the biggest word they have, and the word that is the most creative. The application runs on 2 main parts currently, the Frontend (which handles displaying information and allowing the user to play the game), as well as the Server, or the Backend, which handles the requests from the frontend, as well as the calls to the database.

The frontend runs with NodeJs and Vue, and the backend runs with Python and Django.

If you are reading this in Visual Studio Code, you can Ctrl-Click links to go to them.

# Dependencies

In order to run the application, there are a couple things that need to be downloaded beforehand.

[NodeJs](https://nodejs.org/en/download)
[Python](https://www.python.org/downloads/)

If you plan to run the application through Docker:
[Docker Desktop](www.docker.com/products/docker-desktop/)

# Starting the Application

You can either run the application through Docker, which runs each part of the project in separate containers, or through multiple terminals. Terminals are best for debugging, as they are smaller and quicker, and allow you to run specific commands for development. Docker is better for deploying.

## Docker
Docker is a relatively straightforward and simple way to make "containers", which are virtual environments that docker uses in order to easily run basically any software on anything. It turns data and code into images, which are then turned into actual containers, which run the stuff inside of them.

Docker Compose allows you to group images into a single project or application, and allows very simple building, starting and stopping of entire projects.

Before you do anything with Docker, you need to install [Docker Desktop](www.docker.com/products/docker-desktop/), as well as have it running. Docker commands can only work if Docker Desktop is running in the background. If you see:
```
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```
after using a Docker command, then that means that Docker Desktop is not running, and you should start it.

If you made changes to the project, use:
```
docker compose build
```
in order to make a new image. (Just starting the project again doesn't change the result.)

In order to start the project, use:
```
docker compose up -d
```
-d is used to detach the terminal from the logs of the Docker container.

In order to delete or stop any containers, use:
```
docker compose down
```
(You don't need to stop containers in order to build new images or start those new images, the new images will just replace them once the "docker compose up" command is ran.)

Here is a nice command, which stops the containers, builds new ones, and then starts the project, without needing to do each command separately:
```
docker compose down; docker compose build; docker compose up -d
```

Another small and useful command is:
```
docker system prune
```
The command will remove any unnecessary images and containers from Docker, allowing you to save space. (Docker itself runs in a virtual environment, and so removing anything will not affect your computers space itself, it will just allow Docker's VM to have more space in the future. I know some commands to make Dockers disk smaller, but I won't put them here, since it'll be a bit much.)

*Note*: Your computer might be running some other processes on the ports used by the project, if so, just check out Docker Desktop's UI in order to see what ports they are running on. This really shouldn't be an issue though.

## Commands
If Docker is not working for whatever reason, here are the commands to start each portion of the project.

An advantage to running the commands is that changes to the files are almost instant, rather than needing to re-build both Docker images.

*Note:* You need to run each part in a separate terminal in order for both to run at the same time.

*Secondary Note*: Just like with Docker, other processes might be using the ports the project uses, if so, the terminal should show you where each part of the project is being ran. This is most obvious when you are running multiple of the project at the same time, like having a Docker container running, as well as part of the project in a terminal.

### Frontend
Installing NPM Modules:
```
cd frontend
npm install
```

You also will need to make a copy of the .env.example file, named ".env". It contains the information that shouldn't need to be changed often. For the frontend, this information is the url to the backend.

An easy copy command is:
```
copy .env.example .env
```

You'll still need to manually insert the information into the new .env file, but if there are default values (like the development url for the backend), this keeps them.

**DO NOT ADD PRIVATE INFORMATION INTO .env.example FILES, AS THEY GET SENT TO THE GITHUB**

```
cd frontend
npm run dev
```

You can also run:
```
cd frontend
npm run serve
```

In order to run the frontend on the IP: 0.0.0.0:3000, which is used for Docker. This one also takes slightly longer to start.

After running the commands, the frontend will be running [here](http://localhost:3000).

### Backend

**Make sure you run this in a separate terminal.**

You only have to run these commands once.
*As the project updates, you might need to run these again.*
Also make sure you are in the server directory.

This one installs required modules.
```
pip install -r requirements.txt
```

You also will need to make a copy of the .env.example file, named ".env". It contains the information that shouldn't need to be changed often. For the backend, this information is the username and password to the email we use to send emails.

An easy copy command is:
```
copy .env.example .env
```

You'll still need to manually insert the information into the new .env file, but if there are default values, this keeps them.

**DO NOT ADD PRIVATE INFORMATION INTO .env.example FILES, AS THEY GET SENT TO THE GITHUB**

To update the requirements file, use: 
(This takes the things you have installed through pip, and puts them into a text file. You should use a virtual python environment if you plan to do this, as you might add unnecessary modules to the requirements file.)
```
pip freeze > requirements.txt
```

This one creates the database with migrations we make to the database.
```
python manage.py migrate
```

If you make or update database models, run this: (This will cause new migrations to be made, which will then require you to run the previous command.)
```
python manage.py makemigrations wordhoarderserver
```

This one creates a superuser with the username admin and email admin@example.com. It will also prompt you to make a password as well.
```
python manage.py createsuperuser --username admin --email admin@example.com
```

Run this to start the server:
```
cd server
python manage.py runserver
```

After running the command, the backend server will be running [here](http://localhost:8000) (Although the link itself might not show anything).

It is best to use a python virtual environment, that way we can easily keep track of the modules we use in our project, and so we only install what we need. Here are some of the commands for that.

Starting a new environment (make sure you are in the server folder)
```
cd server
python venv <name of venv folder, i use .venv>
```

To use the venv:
```
./<name>/Scripts/activate
```

Exiting the venv
```
exit
```