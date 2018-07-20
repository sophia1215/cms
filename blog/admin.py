from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.

admin.site.site_header = '管理者後台'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created', 'status')
    list_filter = ('status','created', 'published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

# admin.site.register(Post)
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)

