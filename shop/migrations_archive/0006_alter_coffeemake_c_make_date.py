# Generated by Django 4.0.4 on 2022-05-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_coffeemake_c_make_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemake',
            name='c_make_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Elkészül:'),
        ),
    ]
