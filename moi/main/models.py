from django.db import models

class Image(models.Model):
    alt = models.CharField(max_length=30, default="Изображение")
    path = models.ImageField(upload_to='route_images/general/')

    def __str__(self):
        return self.alt

class Type(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=40)
    descripion = models.TextField(max_length=1000)
    difficult = models.PositiveIntegerField(default=1, choices=((i,i) for i in range(1, 10)))
    lenght = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='main/routes_files/images/additional/')
    gpx = models.FileField(upload_to='main/routes_files/gpx/', max_length=100)
    type = models.ForeignKey(Type, on_delete=models.PROTECT) #Поставить on_delete=models.SET_DEFAULT
    additional_images = models.ManyToManyField(Image)
    
    def __str__(self):
        return self.name