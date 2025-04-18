from django.db import models
from django.contrib.auth.models import User


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    profissao = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.profissao}"


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.IntegerField()


    def __str__(self):
        return self.nome


class Entrega(models.Model):
    nome = models.CharField(max_length=100)
    data_entrega = models.DateField()
    entregue = models.BooleanField()


    def __str__(self):
        return self.nome
    
class Post(models.Model):
    class Status(models.TextChoices):
        revisao = 'R', 'Revisao'
        publicado = 'P', 'Publicado'
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.revisao)


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.imagem}"