# Generated by Django 3.1.6 on 2021-02-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200304_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img1',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='img2',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
