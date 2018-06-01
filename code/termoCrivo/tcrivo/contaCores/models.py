from django.db import models

# Create your models here.
class ContaCores(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField()
    foto = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.nome