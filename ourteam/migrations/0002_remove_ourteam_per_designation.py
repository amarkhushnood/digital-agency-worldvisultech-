# Generated by Django 4.2.6 on 2024-01-28 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourteam',
            name='per_designation',
        ),
    ]