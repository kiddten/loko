# Generated by Django 2.1.5 on 2019-02-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='trains',
            field=models.ManyToManyField(to='ldata.Train'),
        ),
    ]