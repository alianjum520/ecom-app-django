# Generated by Django 3.2.2 on 2021-05-14 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0009_alter_contact_email_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='messages',
        ),
    ]