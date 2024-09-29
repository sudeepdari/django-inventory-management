from django.db import models

# Create your models here.

class Items(models.Model):
    """
    Model to manage Items of the inventory, if required more details can be added here.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    