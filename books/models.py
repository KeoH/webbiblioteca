from django.db import models

from authors.models import Author
from editors.models import Editor


class Theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Tema'


class Book(models.Model):

    registro = models.CharField(max_length=10, default="0000-A", blank=True)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    theme = models.ManyToManyField(Theme)
    pub_year = models.CharField(max_length=4, default="2014")
    resume = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Libro'
