from django.db import models

# Create your models here.


class Student(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    

    def __str__(self):
        return self.fname
    