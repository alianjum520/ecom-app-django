# Generated by Django 3.2.2 on 2021-05-19 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0004_orderitem_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OrderApp.order'),
        ),
    ]
