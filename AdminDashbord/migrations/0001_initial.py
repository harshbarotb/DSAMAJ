# Generated by Django 3.0.5 on 2020-05-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAndEventsBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsTitle', models.CharField(max_length=500)),
                ('NewsDate', models.DateField()),
                ('NewsThumbnailTitleNews', models.CharField(max_length=200)),
                ('NewsImages', models.ImageField(upload_to='newsImages')),
                ('NewsBlogNews', models.CharField(max_length=5000)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
