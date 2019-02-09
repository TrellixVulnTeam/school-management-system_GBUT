from . import views

from django.urls import path



app_name = "index"

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('price/', views.price, name='price'),
	path('news/', views.news, name='news'),
	path('gallery/', views.gallery, name='gallery'),
	path('gallery/', views.gallery, name='gallery'),
	path('news_detail/<slug:id>/', views.news_detail, name='news_detail'),
	


]