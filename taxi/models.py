from django.db import models

# Create your models here.
class Credit(models.Model):
 Amount = models.FloatField()
 phone_number = models.CharField(max_length=100)
 credit = models.FloatField()
 date = models.DateTimeField(auto_now_add=True)
#addthumnial later
#add in author later