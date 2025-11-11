Django ORM Cash Register
=====================

The following program uses the Django ORM to create the Cash Register MVC App as was done in Assignment 2. Instructions for setup are below.

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
```bash
python -m venv venv; source venv/bin/activate; pip install django
```

Initialize the database
```bash
python manage.py makemigrations db; python manage.py migrate
```

Run the project
```bash
python main.py
```

# Running the Script

Run:

```bash
python main.py
```

In the following window, enter a 5-digit UPC code and then click Enter to see the resulting data on the window.
