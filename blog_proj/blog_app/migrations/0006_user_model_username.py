# Generated by Django 4.2 on 2023-05-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_remove_user_model_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_model',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]