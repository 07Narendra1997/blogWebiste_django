# Generated by Django 5.0.6 on 2024-05-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_Img',
            field=models.ImageField(upload_to='blog/static/image'),
        ),
    ]