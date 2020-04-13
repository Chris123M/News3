from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article
from .models import Article



def homepage(request):
    return render(request, 'homepage.html')
    #return HttpResponse('homepage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('about')

def news_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/news_list.html',{'articles': articles})
    #return HttpResponse('Newslist', articles)





