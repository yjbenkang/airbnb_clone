# Generated by Django 2.2.5 on 2021-02-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210227_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'Other'), ('female', 'Female'), ('male', 'Male')], max_length=10),
        ),
    ]
