from django.db import models

class Product(models.Model):
    upc = models.CharField(max_length=32, unique=True, db_index=True)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.upc})"