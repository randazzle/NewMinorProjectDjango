from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):	# *args, **kwargs
    articles = Article.objects.all().order_by('-date')[0:3]
    cards = Article.objects.all().order_by('-date')[3:6]
    #return render(request, 'articles/article_list.html', {'articles':articles})
    return render(request, 'articles/article_list.html', context={'articles':articles, 'cards':cards})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
