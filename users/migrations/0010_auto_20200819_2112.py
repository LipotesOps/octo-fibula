# Generated by Django 2.2 on 2020-08-19 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200819_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_secret',
            field=models.UUIDField(default=uuid.UUID('d9669812-5447-4051-a2b4-ed0b1642049b')),
        ),
    ]
