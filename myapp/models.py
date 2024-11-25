from django.db import models

# Create your models here.

class Login_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

class Diver_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.CharField(max_length=100, null=True, blank=True)
    Post = models.CharField(max_length=100, null=True, blank=True)
    Vehicletype = models.CharField(max_length=100, null=True, blank=True)
    Licenseno = models.IntegerField(null=True, blank=True)
    Vehicleno = models.CharField(max_length=100, null=True, blank=True)
    Phoneno = models.IntegerField(null=True, blank=True)


class User_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname= models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Phoneno = models.IntegerField(null=True, blank=True)


class Complaint_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=100, null=True, blank=True)
    reply = models.CharField(max_length=100 , null=True, blank=True)


class Feedback_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=100, null=True, blank=True)