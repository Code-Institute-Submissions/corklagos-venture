# Generated by Django 3.0.6 on 2020-06-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_orderlineitem_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address',
        ),
    ]