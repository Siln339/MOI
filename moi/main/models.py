from django.db import models

class Image(models.Model):
    alt = models.CharField(max_length=30, default="Изображение")
    path = models.ImageField(upload_to='main/routes_files/images')

    def __str__(self):
        return str(self.id) + '-' + self.alt
    
class Placemark(models.Model):
    name = models.CharField(max_length=40)
    descripion = models.TextField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=40)
    descripion = models.TextField(max_length=1000)
    difficult = models.PositiveIntegerField(default=1, choices=((i,i) for i in range(1, 10)))
    lenght = models.PositiveIntegerField()
    main_image  = models.ForeignKey(Image, on_delete=models.PROTECT, related_name='main_image')
    gpx = models.FileField(upload_to='main/routes_files/gpx/', max_length=100)
    type = models.ForeignKey(Type, on_delete=models.PROTECT) #Поставить on_delete=models.SET_DEFAULT
    additional_images = models.ManyToManyField(Image, related_name='additional_images')
    placemarks = models.ManyToManyField(Placemark)
    
    def __str__(self):
        return self.name