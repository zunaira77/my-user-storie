from django.urls import path 
from . import views 
urlpatterns = [     
    path('', views.post_list, name='post_list'),     
    path('post/<int:pk>/', views.post_detail, name='post_detail'),     
    path('post/new/', views.post_new, name='post_new'), 
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.post_easy, name='post_easy'),
    path('', views.post_medium, name='post_medium'),
    path('', views.post_hard, name='post_hard'),
]