from django.db import models

# Create your models here.
class Credit(models.Model):
    amount = models.FloatField()
    phone_number = models.CharField(max_length=15)
    credit = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class feedback(models.Model):
    username = models.CharField(max_length=30)
    feedback = models.TextField()
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    