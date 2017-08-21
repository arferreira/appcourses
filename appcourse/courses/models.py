from django.db import models

class Course(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='Título')
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(blank=True, verbose_name='Descrição')
    start_date = models.DateField(null=True, blank=True, verbose_name='Data de Início')
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
