# Generated by Django 2.2.5 on 2021-06-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_auto_20210613_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
