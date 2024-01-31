from django.db import models

# Create your models here.

class signup(models.Model):
    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female')
    )
    firstname= models.CharField(max_length=100, null=True)
    lastname= models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    username= models.CharField(max_length=100,null=True)
    phone= models.IntegerField()
    gender =models.CharField(choices=GENDER_CHOICES, max_length=100, null=True)
    image =models.ImageField(null=True, blank=True,upload_to='images/')
    password=models.CharField(max_length=100,null=True)
    confirm_password= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.username
