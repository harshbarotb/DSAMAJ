# Generated by Django 3.0.5 on 2020-05-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserEntry', '0003_auto_20200523_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyhead',
            name='profile_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
