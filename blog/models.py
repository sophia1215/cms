
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# category
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Post
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # category = models.ForeignKey(Category)
    # Add on_delete=models.CASCADE
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
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

