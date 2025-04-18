from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from AppPortal.models import Estudante, Post, Avatar




class MeuAppTests(TestCase):


    def setUp(self):
        """Configuração inicial para os testes"""
        self.user = User.objects.create_user(username='teste', password='12345')


    def test_pagina_home(self):
        """Teste se a página inicial carrega corretamente"""
        response = self.client.get(reverse('home'))  # Testa a URL nomeada 'home'
        self.assertEqual(response.status_code, 200)  # Deve retornar HTTP 200


    def test_login_usuario(self):
        """Teste de login do usuário"""
        login = self.client.login(username='teste', password='12345')
        self.assertTrue(login)  # O login deve ser bem-sucedido




class AvatarModelTest(TestCase):


    def test_criar_avatar(self):
        """Verifica se um avatar pode ser criado corretamente"""
        user = User.objects.create(username='teste')
        avatar = Avatar.objects.create(user=user, imagem='avatares/teste.png')
        self.assertEqual(str(avatar), f"{user.username} - {avatar.imagem}")




class PostModelTest(TestCase):


    def setUp(self):
        """Configuração inicial: Criar um usuário de teste e um post"""
        self.user = User.objects.create_user(username='autor_teste', password='12345')
        self.post = Post.objects.create(
            titulo="Meu primeiro post",
            conteudo="Isso é um teste.",
            autor=self.user,
            status=Post.Status.publicado
        )


    def test_criacao_post(self):
        """Verifica se o post foi criado corretamente"""
        self.assertEqual(self.post.titulo, "Meu primeiro post")
        self.assertEqual(self.post.conteudo, "Isso é um teste.")
        self.assertEqual(self.post.autor.username, "autor_teste")
        self.assertEqual(self.post.status, Post.Status.publicado)


    def test_str_post(self):
        """Verifica se o método __str__ exibe o título corretamente"""
        self.assertEqual(str(self.post), "Meu primeiro post")




class EstudanteModelTest(TestCase):


    def setUp(self):
        """Configuração inicial: Criar um estudante"""
        self.estudante = Estudante.objects.create(
            nome="João",
            sobrenome="Silva",
            email="joao@email.com"
        )


    def test_criacao_estudante(self):
        """Verifica se o estudante foi criado corretamente"""
        self.assertEqual(self.estudante.nome, "João")
        self.assertEqual(self.estudante.sobrenome, "Silva")
        self.assertEqual(self.estudante.email, "joao@email.com")


    def test_str_estudante(self):
        """Verifica se o método __str__ exibe o nome e sobrenome corretamente"""
        self.assertEqual(str(self.estudante), "João Silva")
