# NoteTaker

Notetaker - A Simple Note Taking app created in Flask

# Building Project

## Step 1 :

Cloning the Project

```console
$ git clone https://github.com/PrathameshThorat1729/NoteTaker.git NoteTaker
$ cd NoteTaker
```

## Step 2 :

Creating and Activating Python Virtual Enviroment

```console
$ pip install virtualenv
$ python -m virtualenv env
```

### Activating Virtual Env.

in Windows,

```console
$ & .\env\Scripts\activate
```

in Linux and MacOS,

```console
$ source ./env/bin/activate
```

## Step 3 :

installing required dependencies

```console
$ pip install -r requirements.txt
```

## Step 4 :

edit the databse configuration of app in _config.py_

```python
# ... config.py
# Mysql Database Configuration
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "notetaker"
```

## Step 5 :

creating MySQL database for Schema file

```console
$ mysql -u <username> -p -e "SOURCE SETUP_SCHEMA.sql"
```

Note : User Permissions granted User

## Step 6 :

running the Project

```console
$ python app.py
```
