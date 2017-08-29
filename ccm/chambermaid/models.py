from django.db import models
from django.utils import timezone


class Patient(models.Model):
    SEX = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=11)
    sex = models.CharField(max_length=1, choices=SEX)
    date_joined = models.DateTimeField(default=timezone.now(),editable=False)




