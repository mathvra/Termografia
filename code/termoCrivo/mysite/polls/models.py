from django.db import models
from .cores import percent

# Create your models here.

class paciente(models.Model, percent):
    ident = models.CharField(max_length=200)
    cad_date = models.DateTimeField('Data de cadastro: ')
    imagemImport = models.FilePathField(path="mysite/polls", match='teste2.jpeg')