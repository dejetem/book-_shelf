# Generated by Django 4.0.4 on 2022-05-10 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookapp', '0007_remove_category_books_remove_category_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='categories', to='bookapp.book'),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]