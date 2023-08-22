from django.db import models

# Create your models here.
class Credit(models.Model):
    amount = models.FloatField()
    phonenumber = models.CharField(max_length=1000)
    Credit = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)