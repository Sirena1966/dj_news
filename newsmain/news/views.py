from django.shortcuts import render
from .models import News

# Create your views here.

def home(request):
    news = {
        'news': News.objects.all()
    }
    return render(request, 'news/index.html', news)