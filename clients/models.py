from django.db import models

# Create your models here.

class Client(models.Model):
    #basic personal info
    full_name=models.CharField(max_length=255)
    national_id=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=20)
    address=models.TextField()
    #optional client status
    status = models.CharField(max_length=50,choices=[
        ('active','Active'),
        ('inactive','Inactive')
    ],default='active')

    def __str__(self):
        return self.full_name
