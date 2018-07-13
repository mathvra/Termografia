from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContaCores(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField()
    foto = models.ImageField(default='default.png', blank=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
