from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Jogos(Base):
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    ano_lancamento = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

        def __str__(self):
            return self.nome
            
