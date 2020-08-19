# Generated by Django 2.2 on 2020-08-19 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow_manage', '0002_auto_20200819_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bpmn',
            options={'ordering': ['-id'], 'verbose_name': 'flow_bpmn', 'verbose_name_plural': 'flow_bpmns'},
        ),
        migrations.AlterModelOptions(
            name='flowcategory',
            options={'ordering': ['-id'], 'verbose_name': 'flow_category', 'verbose_name_plural': '流程分类定义，便于维护'},
        ),
        migrations.AlterModelTable(
            name='bpmn',
            table='flow_bpmn',
        ),
        migrations.AlterModelTable(
            name='flowcategory',
            table='flow_category',
        ),
        migrations.AlterModelTable(
            name='flowdefinition',
            table='flow_definition',
        ),
    ]
