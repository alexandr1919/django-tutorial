from django import template
from news.models import Category, News

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}

@register.inclusion_tag('news/news_component.html')
def show_news_block(request, news_id):
    news = News.objects.filter(news_id)
    return {"item": news}
