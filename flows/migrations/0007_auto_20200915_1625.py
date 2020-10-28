# Generated by Django 2.2 on 2020-09-15 08:25

from django.db import migrations, models
import flows.models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0006_flowinstance_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="flowinstance",
            name="num",
            field=models.CharField(
                default=flows.models.genOrderNum, editable=False, max_length=32
            ),
        ),
        migrations.AlterField(
            model_name="flowinstance",
            name="name",
            field=models.CharField(max_length=64),
        ),
    ]
