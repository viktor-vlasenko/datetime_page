# Generated by Django 2.0 on 2018-01-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
    ]