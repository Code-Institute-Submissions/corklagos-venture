# Generated by Django 3.0.6 on 2020-06-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(choices=[('', 'See all'), ('engines', 'Engines'), ('gearboxes', 'Gear Boxes'), ('lamps', 'Lamps'), ('Radiators', 'radiators'), ('bumpers', 'Bumpers')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='listing',
        ),
    ]