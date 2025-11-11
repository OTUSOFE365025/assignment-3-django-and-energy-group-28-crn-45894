# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # folder where settings.py lives

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),   # <- single, predictable file
    }
}

INSTALLED_APPS = [
    "db",
    "django.contrib.contenttypes",
    "django.contrib.auth",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"