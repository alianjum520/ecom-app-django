# Generated by Django 3.2.2 on 2021-05-18 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]