# Generated by Django 2.1.4 on 2019-01-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('num', models.IntegerField()),
                ('places_to_travel', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]