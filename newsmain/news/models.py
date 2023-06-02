from django.db import models

# Create your models here.

class Author(models.Model):
    surname = models.CharField('Фамалия', max_length=50)

    def __str__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Фамилия'
        verbose_name_plural = 'Фамилии'

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    src = models.CharField('Картинка', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
