# Generated by Django 4.0.4 on 2022-06-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0001_initial'),
        ('shop', '0005_alter_coffeemake_c_make_dose_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeorder',
            name='sugar_choice',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to='raw_material.productacquisition', verbose_name='Lefoglalt Cukor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffeeorder',
            name='coffee_dose',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Kávé [0,5-2] Adag'),
        ),
        migrations.AlterField(
            model_name='coffeeorder',
            name='flavour_dose',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Ízesítő [0,5-2] Adag [5 g]'),
        ),
        migrations.AlterField(
            model_name='coffeeorder',
            name='milk_dose',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Tej [0,5-4] Adag [50 ml]'),
        ),
        migrations.AlterField(
            model_name='coffeeorder',
            name='sugar_dose',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Cukor [0,5-3] Adag [5 g]'),
        ),
    ]
