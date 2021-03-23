from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),  #url, home class from views, name of the page is blog-home
    path('about/', views.about, name='blog-about'),
]