from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete =  models.CASCADE,
        primary_key = True
    )

    experience = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username
    
class Image(models.Model):
    alt = models.CharField(max_length=30)
    path = models.ImageField(upload_to='route_images/general/')

    def __str__(self):
        return self.alt

class Type(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=40)
    descripion = models.CharField(max_length=300)
    difficult = models.IntegerField()
    lenght = models.IntegerField()
    main_image = models.ImageField(upload_to='route_images/additional/')
    gpx = models.FileField(upload_to='route_gpx/', max_length=100)
    type = models.ForeignKey(Type, on_delete=models.PROTECT) #Поставить on_delete=models.SET_DEFAULT
    additional_images = models.ManyToManyField(Image)