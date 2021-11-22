from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
CURRENCY = settings.CURRENCY




class Restauran_ubicacion(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(unique=True, max_length=150)
    latitude = models.DecimalField(max_digits=18, decimal_places=6)
    longitude = models.DecimalField(max_digits=19, decimal_places=6)



    def __str__(self):
        return self.title

class restaurant(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    """value = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=False)"""
    Restauran_ubicacion = models.ForeignKey(Restauran_ubicacion, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


    def tag_category(self):
        return f'{self.Restauran_ubicacion.title}'
