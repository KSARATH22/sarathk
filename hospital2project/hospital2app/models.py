from django.db import models

class Doctors(models.Model):

    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    mobile=models.BigIntegerField()
    addres=models.CharField(max_length=400)
    def __str__(self):
        return self.first_name

class Patients(models.Model):

    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    pat_age=models.IntegerField()
    pat_gender=models.CharField(max_length=200)
    mobile=models.BigIntegerField()
    addres=models.CharField(max_length=300)
    def __str__(self):
        return self.first_name

class Nurses(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    mobile=models.BigIntegerField()
    addres=models.CharField(max_length=300)
    def __str__(self):
        return self.first_name
class Reports(models.Model):
    case = models.CharField(max_length=200)
    lab_attendant=models.CharField(max_length=300)

    description=models.CharField(max_length=200)
    def __str__(self):
        return self.case
class Messages(models.Model):
    name=models.CharField(max_length=300)
    datetime=models.DateField()
    message=models.CharField(max_length=200)
    rating=models.IntegerField()
    def __str__(self):
        return self.name
class ContactData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    def __str__(self):
        return self.first_name


class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    time = models.DateField()
    feedback = models.CharField(max_length=500)
