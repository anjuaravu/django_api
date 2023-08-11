from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.BigAutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()

    # def __str__(self):
    #     return self.product_name


class Customer_preference(models.Model):
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    preference_id = models.CharField(max_length=100)


class Orders(models.Model):
    preference_id = models.ForeignKey(Customer_preference, on_delete=models.CASCADE)
    customer_id=models.CharField(max_length=100)
    order_date=models.DateField()