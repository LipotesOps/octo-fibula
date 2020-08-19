# Generated by Django 2.2 on 2020-08-19 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow_manage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BPMN20XML',
            new_name='BPMN',
        ),
        migrations.AlterModelOptions(
            name='bpmn',
            options={'ordering': ['-id'], 'verbose_name': 'bpmn', 'verbose_name_plural': 'bpmns'},
        ),
        migrations.AlterModelOptions(
            name='flowdefinition',
            options={'ordering': ['-id'], 'verbose_name': 'flow_definition', 'verbose_name_plural': '流程定义'},
        ),
        migrations.AlterModelTable(
            name='bpmn',
            table='bpmn',
        ),
        migrations.AlterModelTable(
            name='flowcategory',
            table='flowcategory',
        ),
        migrations.AlterModelTable(
            name='flowdefinition',
            table='FlowDefinition',
        ),
    ]
