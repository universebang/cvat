# Generated by Django 2.1.5 on 2019-02-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0027_auto_20190206_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='segment_size',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
