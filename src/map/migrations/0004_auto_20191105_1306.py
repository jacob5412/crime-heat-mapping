# Generated by Django 2.2.6 on 2019-11-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_news_statecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(max_length=55),
        ),
    ]