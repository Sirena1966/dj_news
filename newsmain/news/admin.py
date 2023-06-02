from django.contrib import admin
from .models import News, Author, Genre

admin.site.register(News)
admin.site.register(Author)
admin.site.register(Genre)
# Register your models here.
