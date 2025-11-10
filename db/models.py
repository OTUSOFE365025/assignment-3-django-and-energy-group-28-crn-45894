import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# Product class
class Product(models.Model):
    upc = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f"{self.upc} {self.name} %.2f" % self.price