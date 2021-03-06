# Generated by Django 3.0.5 on 2020-05-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
                ('Cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('Name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('Accomodation', models.BooleanField()),
                ('Events', models.ManyToManyField(blank=True, to='users.Event')),
            ],
        ),
    ]
