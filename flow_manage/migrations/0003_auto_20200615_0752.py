# Generated by Django 2.2 on 2020-06-15 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flow_manage', '0002_processdefinition_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='processdefinition',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processdefinition',
            name='mtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='修改时间'),
            preserve_default=False,
        ),
    ]