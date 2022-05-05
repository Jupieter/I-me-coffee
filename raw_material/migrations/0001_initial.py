# Generated by Django 4.0.4 on 2022-05-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('material1', models.IntegerField(default=0)),
                ('material2', models.IntegerField(default=0)),
                ('material3', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='WareData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ware_type', models.CharField(max_length=50)),
                ('ware_brand', models.CharField(max_length=50)),
                ('ware_brand_name', models.CharField(max_length=50)),
                ('package_weight', models.IntegerField(default=0)),
                ('ware_price', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]