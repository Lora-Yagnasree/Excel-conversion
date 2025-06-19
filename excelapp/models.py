from django.db import models
# models.py
from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
