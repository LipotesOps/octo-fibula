# Generated by Django 2.2 on 2020-09-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0008_flowinstance_completed"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskinstance",
            name="status",
            field=models.CharField(
                choices=[
                    ("running", "进行中"),
                    ("completed", "已完成"),
                    ("rejected", "已拒绝"),
                    ("cancled", "已撤回"),
                ],
                default="running",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="flowbpmn",
            name="status",
            field=models.CharField(
                choices=[("draft", "草稿"), ("deployed", "已部署"), ("del", "删除")],
                default="draft",
                max_length=16,
            ),
        ),
    ]
