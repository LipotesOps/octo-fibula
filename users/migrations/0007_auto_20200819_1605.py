# Generated by Django 2.2 on 2020-08-19 08:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200819_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_secret',
            field=models.UUIDField(default=uuid.UUID('b68048c4-6f00-408b-be51-b512b3ff0624')),
        ),
    ]
