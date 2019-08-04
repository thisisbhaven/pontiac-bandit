from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(max_length=20, primary_key=True)
    category_id = models.CharField(max_length=20)
    subcategory_id = models.CharField(max_length=20)
    manufacturer_id = models.CharField(max_length=20)
    selling_price_per_unit = models.FloatField()

    def __str__(self):
        return str(self.product_id)

class Customer(models.Model):
    customer_id = models.AutoField(max_length=20, primary_key=True)
    society_id = models.CharField(max_length=20)
    city_id = models.CharField(max_length=20)

    def __str__(self):
        return str(self.customer_id)

class Order(models.Model):
    order_id = models.AutoField(max_length=20, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    route_id = models.CharField(max_length=20, default=0)
    store_id = models.CharField(max_length=20)
    order_date = models.CharField(max_length=20)
    product_quantity = models.IntegerField()
    total_cost = models.IntegerField()
    product_added_to_basket_on = models.CharField(max_length=20)
    subscription = models.BooleanField(default=0)

    def __str__(self):
        return str(self.order_id)

class BPM(models.Model):
    customer_id = models.AutoField(max_length=10, primary_key=True)
    r1 = models.CharField(max_length=20)
    r2 = models.CharField(max_length=20)
    r3 = models.CharField(max_length=20)
    r4 = models.CharField(max_length=20)
    r5 = models.CharField(max_length=20)
    r6 = models.CharField(max_length=20)
    r7 = models.CharField(max_length=20)
    r8 = models.CharField(max_length=20)
    r9 = models.CharField(max_length=20)
    r10 = models.CharField(max_length=20)

    def __str__(self):
        return str(self.customer_id)