# Generated by Django 4.2.6 on 2024-01-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ourteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_icon', models.CharField(max_length=50)),
                ('per_name', models.CharField(max_length=50)),
                ('per_designation', models.CharField(max_length=50)),
            ],
        ),
    ]
