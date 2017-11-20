from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fotos(models.Model):
	imagem = models.ImageField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	titulo = models.CharField(max_length = 50, default = 'teste')
	data_postagem = models.DateTimeField(auto_now_add=True)

