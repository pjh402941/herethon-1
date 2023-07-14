# Generated by Django 3.2 on 2023-07-14 08:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boardapp', '0004_board_address_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='applied_users',
            field=models.ManyToManyField(blank=True, related_name='applied_boards', to=settings.AUTH_USER_MODEL),
        ),
    ]