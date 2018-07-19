
from django.db import models
from django.utils import timezone
from django.urls import reverse

# include the User model
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=160)
    # Add on_delete=models.CASCADE
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE,)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
        # return reverse('blog:post_detail', args=[self.id])

    def __str__(self):
        return self.title

