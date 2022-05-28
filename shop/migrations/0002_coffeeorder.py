# Generated by Django 4.0.4 on 2022-05-28 07:53

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_dose', models.IntegerField(default=1, verbose_name='Kávé Adag')),
                ('sugar_dose', models.IntegerField(default=1, verbose_name='Cukor Adag')),
                ('milk_dose', models.IntegerField(default=1, verbose_name='Tej Adag')),
                ('coffee_reg', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Rögzítés dátuma')),
                ('coffe_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.coffeemake', verbose_name='Lefoglalt Kávé')),
                ('coffe_user', models.ForeignKey(default=accounts.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Lefoglalta', to=settings.AUTH_USER_MODEL, verbose_name='Lefoglalta')),
            ],
        ),
    ]
