# Generated by Django 3.2.8 on 2022-01-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(1, 'perro'), (2, 'gato'), (3, 'otros')], default=1)),
                ('edad', models.FloatField(max_length=100)),
                ('propietario', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'mascotas',
            },
        ),
    ]
