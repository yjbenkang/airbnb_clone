# Generated by Django 2.2.5 on 2021-02-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210226_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
