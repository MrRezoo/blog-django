from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')


class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    objects = models.Manager()
    published = PublishedArticleManager()

    def __str__(self):
        return f"{self.title} #{self.writer}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('blog_app:article_detail', args=[self.id, self.slug])
