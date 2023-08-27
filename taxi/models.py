from django.db import models

# Create your models here.
class Credit(models.Model):
    amount = models.FloatField()
    phone_number = models.CharField(max_length=15)
    credit = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    