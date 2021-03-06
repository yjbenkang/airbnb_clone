# Generated by Django 2.2.5 on 2021-05-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0010_auto_20210526_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], default='pending', max_length=12),
        ),
    ]
