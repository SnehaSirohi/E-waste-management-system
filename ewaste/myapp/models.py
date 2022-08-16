from math import degrees
from django.db import models
from django.contrib.auth.forms import User

class extendeduser(models.Model):
     name = models.CharField(max_length=20)
     aadhaar_no = models.CharField(max_length=20, null = True)
     email =  models.CharField(max_length = 12,null= True)
     password = models.CharField(max_length = 20,null = True)
     username = models.CharField(max_length = 20,null = True)
     def __str__(self):
        return self.name
