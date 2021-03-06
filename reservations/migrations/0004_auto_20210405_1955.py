# Generated by Django 2.2.5 on 2021-04-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20210405_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
