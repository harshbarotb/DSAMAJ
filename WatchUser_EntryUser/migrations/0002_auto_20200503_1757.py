# Generated by Django 3.0.5 on 2020-05-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WatchUser_EntryUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='female',
            name='Zone_Code',
            field=models.ManyToManyField(max_length=50, to='WatchUser_EntryUser.ZoneCode', verbose_name='List Of ZoneCode'),
        ),
        migrations.AlterField(
            model_name='headperson',
            name='Zone_Code',
            field=models.ManyToManyField(max_length=50, to='WatchUser_EntryUser.ZoneCode'),
        ),
        migrations.AlterField(
            model_name='headperson',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'male'), (2, 'female'), (3, 'not specified')], default=' '),
        ),
        migrations.AlterField(
            model_name='male',
            name='Zone_Code',
            field=models.ManyToManyField(max_length=50, to='WatchUser_EntryUser.ZoneCode', verbose_name='List Of ZoneCode'),
        ),
    ]
