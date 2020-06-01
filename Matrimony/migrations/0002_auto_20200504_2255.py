# Generated by Django 3.0.5 on 2020-05-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matrimony', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonyuserreg',
            name='Age',
            field=models.CharField(choices=[(9, '--------'), (0, '18 to 20'), (1, '20 to 25'), (2, '26 to 30'), (3, '31 to 35'), (4, '36 to 40'), (5, '41 to 45'), (6, '45 to 50'), (7, '50 to 55'), (8, '55 to 60')], default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='matrimonyuserreg',
            name='Father_PhoneNo',
            field=models.CharField(max_length=30),
        ),
    ]
