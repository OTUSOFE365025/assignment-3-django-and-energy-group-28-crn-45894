Django ORM Cash Register
=====================

Use the database components of Django without having to use the rest of Django (i.e. running a web server)! :tada: A typical use case for using this template would be if you are writing a python script and you would like the database functionality provided by Django, but have no need for the request/response functionalty of a client/server web application that Django also provides. 

With this project template you can write regular python scripts and use Django's excellent ORM functionality with the database backend of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

## Requirements

- Python 3.9+
- Python packages:
  - `venv`
  - `django`
  - `PyQt6`
  - `pyqt6_sip`
- **Dependencies can be found and installed from the `requirements.txt` file** 

## Repository Structure

```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── requirements.txt
├── products.txt
├── README.md
└── settings.py
```

## Quick Setup

1. **Clone the repository**

```bash
git clone github.com/OTUSOFE365025/assignment-3-django-and-energy-group-28-crn-45894@latest
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```

# Running the Script

From the src folder, run:

```bash
python main.py
```

In the following window, enter a 5-digit UPC code and then click Enter to see the resulting data on the window.
