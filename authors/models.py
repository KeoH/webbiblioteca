from django.conf import settings
from django.db import models

from .choices import SEX_CHOICES


class Nation(models.Model):
    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="nation/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'País'
        verbose_name_plural = 'Paises'


class Author(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='H')
    photo = models.ImageField(upload_to="author/", blank=True)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
