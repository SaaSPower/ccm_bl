from django.db import models
from django.utils.timezone import now


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
    date_joined = models.DateTimeField(default=now, editable=False)


class RatingScale(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()


class Statement(models.Model):
    TYPE = [
        ('1', 'Numeric Selection'),
        ('2', 'Character Selection'),
        ('3', 'True or False'),
        ('4', 'Text'),
    ]
    id = models.AutoField(primary_key=True)
    rating_scale = models.ForeignKey(RatingScale, db_index=True, on_delete=models.CASCADE)
    sort_index = models.IntegerField(db_index=True)
    statement = models.TextField()
    description = models.TextField()
    question_type = models.CharField(max_length=2, choices=TYPE)
    options = models.TextField()
    answer_index = models.IntegerField


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, db_index=True)
    description = models.TextField()
    rating_scales = models.ManyToManyField(RatingScale, )


class TypeGroup(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(unique=True, max_length=254, db_index=True)
    description = models.TextField()
    model_group = models.ForeignKey(TypeGroup, on_delete=models.CASCADE)


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type)
    date_created = models.DateTimeField(default=now, editable=False)
    medical_history = models.TextField()


class AnswerSheet(models.Model):
    id = models.AutoField(primary_key=True)
    rating_scale = models.ForeignKey(RatingScale, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=254, blank=True)
    answer2 = models.CharField(max_length=254, blank=True)
    answer3 = models.CharField(max_length=254, blank=True)
    answer4 = models.CharField(max_length=254, blank=True)
    answer5 = models.CharField(max_length=254, blank=True)
    answer6 = models.CharField(max_length=254, blank=True)
    answer7 = models.CharField(max_length=254, blank=True)
    answer8 = models.CharField(max_length=254, blank=True)
    answer9 = models.CharField(max_length=254, blank=True)
    answer10 = models.CharField(max_length=254, blank=True)
    answer11 = models.CharField(max_length=254, blank=True)
    answer12 = models.CharField(max_length=254, blank=True)
    answer13 = models.CharField(max_length=254, blank=True)
    answer14 = models.CharField(max_length=254, blank=True)
    answer15 = models.CharField(max_length=254, blank=True)
    answer16 = models.CharField(max_length=254, blank=True)
    answer17 = models.CharField(max_length=254, blank=True)
    answer18 = models.CharField(max_length=254, blank=True)
    answer19 = models.CharField(max_length=254, blank=True)
    answer20 = models.CharField(max_length=254, blank=True)
    answer21 = models.TextField(default='')
    answer22 = models.TextField(default='')
    answer23 = models.TextField(default='')
    answer24 = models.TextField(default='')
    answer25 = models.TextField(default='')
    date_created = models.DateTimeField(default=now, editable=False)



