from django.db import models

# Create your models here
class RFMC(models.Model):
    customer_id = models.AutoField(max_length=10, primary_key=True)
    Recency_flag = models.IntegerField()
    Freq_flag = models.IntegerField()
    monetary_flag = models.IntegerField()

    def __str__(self):
        return str(self.customer_id)

class CP(models.Model):
    customer_id = models.AutoField(max_length=10, primary_key=True)
    Sub_flag = models.IntegerField()
    subscription = models.BooleanField()
    Recency_flag = models.IntegerField()
    Refreq = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return str(self.customer_id)

class RO(models.Model):
    customer_id = models.AutoField(max_length=10, primary_key=True)
    Recency_flag = models.IntegerField()
    monetary_flag = models.IntegerField()

    def __str__(self):
        return str(self.customer_id)