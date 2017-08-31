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
    date_joined = models.DateTimeField(default=timezone.now(), editable=False)


class RatingScale(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating_scales = models.ManyToManyField(RatingScale)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(unique=True, max_length=254)
    description = models.TextField()


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    rating_scale = models.ForeignKey(RatingScale, on_delete=models.CASCADE)
    index = models.IntegerField()
    statement = models.TextField()
    options = models.TextField()


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type)
    date_created = models.DateTimeField(default=timezone.now(), editable=False)
    medical_history = models.TextField()


class AnswerSheet(models.Model):
    id = models.AutoField(primary_key=True)
    rating_scale = models.ForeignKey(RatingScale, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=254)
    answer2 = models.CharField(max_length=254)
    answer3 = models.CharField(max_length=254)
    answer4 = models.CharField(max_length=254)
    answer5 = models.CharField(max_length=254)
    answer6 = models.CharField(max_length=254)
    answer7 = models.CharField(max_length=254)
    answer8 = models.CharField(max_length=254)
    answer9 = models.CharField(max_length=254)
    answer10 = models.CharField(max_length=254)
    answer11 = models.CharField(max_length=254)
    answer12 = models.CharField(max_length=254)
    answer13 = models.CharField(max_length=254)
    answer14 = models.CharField(max_length=254)
    answer15 = models.CharField(max_length=254)
    answer16 = models.CharField(max_length=254)
    answer17 = models.CharField(max_length=254)
    answer18 = models.CharField(max_length=254)
    answer19 = models.CharField(max_length=254)
    answer20 = models.CharField(max_length=254)
    date_created = models.DateTimeField(default=timezone.now(), editable=False)



