# Generated by Django 3.1.3 on 2020-11-06 19:44

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]