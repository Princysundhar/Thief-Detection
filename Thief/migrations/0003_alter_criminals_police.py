# Generated by Django 3.2.21 on 2023-10-04 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Thief', '0002_criminals_police'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminals',
            name='POLICE',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Thief.police_station'),
        ),
    ]
