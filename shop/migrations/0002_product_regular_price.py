# Generated by Django 2.2 on 2020-04-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='regular_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
