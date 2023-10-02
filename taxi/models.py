from django.db import models
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
    

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=100) 
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=100)
