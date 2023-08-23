from django.db import models

# Create your models here.
class Credit(models.Model):
    amount = models.FloatField()
<<<<<<< HEAD
    phonenumber = models.CharField(max_length=1000)
    Credit = models.FloatField()
=======
    phone_number = models.CharField(max_length=15)
    credit = models.FloatField()
>>>>>>> ac0821965a66c3b8df718bcab8cbd71d7814e144
    date = models.DateTimeField(auto_now_add=True)