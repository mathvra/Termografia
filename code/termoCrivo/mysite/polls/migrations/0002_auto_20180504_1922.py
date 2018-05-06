# Generated by Django 2.0.5 on 2018-05-04 22:22

from django.db import migrations, models
import polls.cores


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contaCores',
        ),
        migrations.DeleteModel(
            name='imagemModel',
        ),
        migrations.AddField(
            model_name='paciente',
            name='imagemImport',
            field=models.FilePathField(default=1, match='teste2.jpeg', path='/polls'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='valorPercent',
            field=models.IntegerField(default=1, verbose_name=polls.cores.percent),
            preserve_default=False,
        ),
    ]