# Generated by Django 4.2.10 on 2024-02-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='income',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
