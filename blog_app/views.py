from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog_app/all_articles.html', {'all_articles': articles})


def article_detail(request, id, slug):
    # article = Article.objects.get(id=id, slug=slug)
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog_app/article.html', {'article_detail': article})
