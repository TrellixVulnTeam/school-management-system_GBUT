from django.shortcuts import render
from administrator.models import News
from django.shortcuts import render, get_object_or_404, redirect
def index(request):
	return render(request, 'index.html', {})
def about(request):
	return render(request, 'about.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def price(request):
	return render(request, 'price.html', {})
def news(request):
	detail = News.objects.filter(status='published')
	return render(request, 'news.html', {'detail':detail})
def news_detail(request, id):
	detail = get_object_or_404(News, id=id)
	return render(request, 'newsdetail.html', {'detail':detail})

def gallery(request):
	return render(request, 'gallery.html', {})