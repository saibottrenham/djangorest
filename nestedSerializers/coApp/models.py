from django.db import models


# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.firstName


class Order(models.Model):
    product = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.product
