from django.db import models

# manager for Course
class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(title__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    # definições do modelo
    title = models.CharField(blank=True, max_length=100, verbose_name='Título')
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(blank=True, verbose_name='Descrição')
    about = models.TextField(blank=True, verbose_name='Sobre o curso')
    start_date = models.DateField(null=True, blank=True, verbose_name='Data de Início')
    image = models.ImageField(upload_to='courses/images',
                              null=True, blank=True, verbose_name='Imagem')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    objects = CourseManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['created_at']

    def __str__(self):
        return self.title
