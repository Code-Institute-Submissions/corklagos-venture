# Generated by Django 3.0.6 on 2020-06-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200608_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_price',
            field=models.CharField(max_length=20),
        ),
    ]