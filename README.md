<h1 align="center">
  <br>
  <img src="https://pbs.twimg.com/profile_images/910158554568515584/Gf6WD-iH_400x400.jpg" alt="Fraunhofer" width="300">
  
  <br>
</h1>
<h2 align="center">
  <br>
   <img src="https://teamvirtue.nl/wp-content/uploads/LINQ_Logo_Black-300x138.png" alt="Fraunhofer" width="200">
   <img src="http://www.sollite.net/images/img/2222222-01.jpg" alt="Fraunhofer" width="200">
   <img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Eindhoven_University_of_Technology_logo.svg" alt="Fraunhofer" width="200">
   <img src="https://cdn.worldvectorlogo.com/logos/fontys-39.svg" alt="Fraunhofer" width="200">
  <br>
</h2>

# Setup
## Prerequisites for development enviorment
1. Make sure you have installed `python` on your machine. [Download Python](https://www.python.org/downloads/)
2. `pip` package manager is installed. If you have a version of `python 2 >= 2.7.9 or Python 3 >= 3.4` you will probably have ``pip`` installed if not [download `pip`](https://www.python.org/downloads/) and in **Terminal** run ``` python get-pip.py```. If you have problems [pip documentation](https://pip.pypa.io/en/stable/installing/)
3. This step is not mandatory but recommended is to make a *python virtual environment* ```sudo pip install virtualenv```
    * Unix based operating systems  
      * Installation of **virtualenv** ```sudo pip install virtualenv```
      * Create a directory to hold the project ```mkdir ~/projectname```
      * Create a virtual environment inside the project folder ```virtualenv nameofprojectenv```
    * Windows operating systems
      * Installation of **virtualenv** ```pip install virtualenv```
      * Installation of **virtualenvwrapper-win** ```pip install virtualenvwrapper-win```
      * Navigate to the project folder.
      * Create a virtual environment inside the project folder ```mkvirtualenv nameofprojecten```
4. PostgreSQL is the database in use so make sure you have it installed.  
    * Unix based operating systems
        *  updating system variables via **Terminal** command ``sudo apt-get update`` 
        *  Installing **PostgreSQL** via **Terminal** command ``sudo apt-get install libpq-dev postgresql postgresql-contrib`` *updating system variables*
        *  Your operating system will make a default user name called ```postgres```  log in with the command ```sudo su - postgres``` 
        *  Creating a new database ```CREATE DATABASE databasename```
        *  Creating a new user ```CREATE USER username WITH PASSWORD 'secret'```
        *  To test if you have installed it correctly use command ```psql -U username -d databasename```
    * Windows operationg systems
        *  Go to the PostgreSQL official website, download section for Windows http://www.postgresql.org/download/windows/
        *  Click on the download installer from https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows
        *  Choose the latest version to download. It takes few minutes to complete the download.
        *  If you need help with the installation process visit http://www.postgresqltutorial.com/install-postgresql/
        
## Development environment setup
1. Install all requirments run command in the project directory ```pip install -r requirements.txt```
2. Setting up database, add this code to **setings.py**  
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "databasename",
        "USER": "username",
        "PASSWORD": "secret",
        "HOST": "localhost",
        "PORT": "",
    }
}
```
3. Check if the ```DEBUG = True``` is set in **setings.py**
4. Make migrations for database ```python manage.py makemigrations``` 
5. Migrate **models.py** to postgres with command ```python manage.py migrate```
6. Run a the test server with command ```python manage.py runserver``` this will run the server on the default *port 8000* if that port is taken you can change the port that the test server runs on with ```python manage.py runserver 0.0.0.0:8090```
## Production environment setup
### Coming soon
## Extending a **models.py** for database 
1. 
