# Generated by Django 3.1.6 on 2021-02-17 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Adventure'), ('2', 'Relaxation'), ('3', 'Nature'), ('4', 'Architecture'), ('5', 'Historical'), ('6', 'Religious')], default=('1', 'Adventure'), max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
