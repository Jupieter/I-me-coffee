# Generated by Django 4.0.4 on 2022-05-20 09:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raw_material', '0020_alter_productacquisition_store_status'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoffeeBoile',
            new_name='CoffeeMake',
        ),
        migrations.RenameField(
            model_name='coffeemake',
            old_name='c_boile_date',
            new_name='c_make_date',
        ),
        migrations.RenameField(
            model_name='coffeemake',
            old_name='c_boile_dose',
            new_name='c_make_dose',
        ),
        migrations.RenameField(
            model_name='coffeemake',
            old_name='c_boile_user',
            new_name='c_make_user',
        ),
        migrations.RenameField(
            model_name='coffeemake',
            old_name='c_boile_ware',
            new_name='c_make_ware',
        ),
    ]
