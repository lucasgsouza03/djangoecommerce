from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificados', max_length=100)
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('catalogo:categoria', kwargs={'slug':self.slug})
    

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificados', max_length=100)
    categoria = models.ForeignKey('catalogo.Categoria', verbose_name='Categoria', on_delete=models.DO_NOTHING)
    descricao = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('catalogo:produto', kwargs={'slug':self.slug})
