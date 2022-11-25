from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm

# Create your views here.

# в request хранятся данные о запросе (куки, сессии и тд)
def index(request):
    news = News.objects.all()
    print(news)
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add.html', {'form': form})
