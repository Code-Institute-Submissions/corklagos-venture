# Generated by Django 3.0.6 on 2020-06-09 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0007_auto_20200609_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
