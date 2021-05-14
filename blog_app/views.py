from django.shortcuts import render
from .models import Article


# Create your views here.
def all_articles(request):
    all_articles = Article.objects.all()
    return render(request, 'blog_app/all_articles.html', {'all_articles': all_articles})
