# Generated by Django 4.2 on 2023-05-23 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_alter_post_model_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_model',
            name='user_con',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog_app.user_model'),
            preserve_default=False,
        ),
    ]
