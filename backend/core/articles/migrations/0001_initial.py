# Generated by Django 5.2.4 on 2025-07-30 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category Name', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Article Categories',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Tag Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date Created (auto-filled)')),
                ('image', models.ImageField(help_text='Article Image', upload_to='blog/articles/')),
                ('title', models.CharField(help_text='Article Title', max_length=255)),
                ('content', models.TextField(blank=True, help_text='Article Content (Optional)')),
                ('author', models.ForeignKey(blank=True, help_text='Article Author', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_articles', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(help_text='Article Category (Optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.articlecategory')),
                ('tags', models.ManyToManyField(blank=True, help_text='Tags (Optional)', to='articles.articletag')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date Created (auto-filled)')),
                ('name', models.CharField(help_text='Your name*', max_length=255)),
                ('email', models.EmailField(help_text='Your email*', max_length=254)),
                ('website', models.URLField(blank=True, help_text='Your website (Optional)')),
                ('content', models.TextField(help_text='Your Comment*')),
                ('article', models.ForeignKey(help_text='Related Article', on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('parent', models.ForeignKey(blank=True, help_text='Parent Comment (Optional)', null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articlecomment')),
            ],
        ),
    ]
