from django import template
from news.models import Category, News
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {"categories": categories}

@register.inclusion_tag('news/news_component.html')
def show_news_block(request, news_id):
    news = News.objects.filter(news_id)
    return {"item": news}
