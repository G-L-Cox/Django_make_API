from django.db import models




class stuff_temp(models.Model):
    name = models.CharField(max_length=50)
    stuff = models.CharField(max_length=50)
    num = models.CharField(max_length=50)

    def __str__(self):
        return self.name