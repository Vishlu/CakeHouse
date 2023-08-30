from django.db import models

# Create your models here.
class Userinformation(models.Model):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70)
    email_id = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    cake = models.CharField(max_length=100, default='not have')
    quantity = models.IntegerField(default=1)