# Generated by Django 5.0.6 on 2024-05-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_text',
            field=models.TextField(max_length=1000),
        ),
    ]