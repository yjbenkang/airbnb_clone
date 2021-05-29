# Generated by Django 2.2.5 on 2021-05-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_auto_20210526_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('confirmed', 'Confirmed'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
