# Generated by Django 2.0.5 on 2018-06-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contaCores', '0002_auto_20180601_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacores',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
