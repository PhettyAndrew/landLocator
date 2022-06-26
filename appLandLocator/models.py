from django.db import models

# Create your models here.


class Land(models.Model):
    landCode = models.CharField(max_length=5)
    ph = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    location = models.CharField(max_length=50)
    typeOfSoil = models.CharField(max_length=50)
    soilProperties = models.TextField()
    cost = models.DecimalField(max_digits=1000, decimal_places=2)
    landHistory = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.landCode


class Image(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    image = models.ImageField()

    def get_image(self):
        return self.image