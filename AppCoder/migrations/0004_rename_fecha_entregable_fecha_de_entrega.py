# Generated by Django 4.1.7 on 2023-04-23 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_rename_fecha_entrega_entregable_fecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='fecha',
            new_name='fecha_de_entrega',
        ),
    ]
