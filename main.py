############################################################################
## Django ORM CashRegister
############################################################################

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

# Create product classes using input file (if db is not yet populated)
# Ensure your current working directory is "../assignment-3-django-and-energy-group-28-crn-45894"
if not Product.objects.all():
    with open("products.txt") as infile:
        lines = infile.read().split("\n")

    for line in lines:
        line = line.split(' ')
        Product.objects.create(upc=int(line[0]), name=line[1], price=float(line[2]))

# Temporary Input Handler
scanned_code = int(input("Enter UPC: "))
found_product = Product.objects.get(upc=scanned_code)
print(found_product)