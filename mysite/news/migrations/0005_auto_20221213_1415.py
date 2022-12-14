# Generated by Django 3.2 on 2022-12-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='views_counter',
            field=models.IntegerField(default=0),
        ),
    ]
