# Generated by Django 4.0.4 on 2022-05-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waredata',
            name='package_weight',
            field=models.IntegerField(default=0, verbose_name='Package Weigh [g]'),
        ),
    ]