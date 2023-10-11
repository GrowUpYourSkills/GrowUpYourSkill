from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField()
    country = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    age = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.firstname

class Registration(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField()
    country = models.CharField(max_length=122)
    course = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    age = models.CharField(max_length=122)
    payment_method = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.firstname
    
    
    