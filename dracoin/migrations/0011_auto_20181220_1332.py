# Generated by Django 2.0.9 on 2018-12-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dracoin', '0010_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, db_index=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(db_index=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
