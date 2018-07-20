from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', include([
        path('', views.list_of_post, name='list_of_post'),
        path('<slug:slug>/', views.post_detail, name='post_detail'),
        # path('<int:id>/', views.post_detail, name='post_detail')
        path('category/<slug:category_slug>/', views.list_of_post_by_category, name='list_of_post_by_category'),
    # ]))    
]

