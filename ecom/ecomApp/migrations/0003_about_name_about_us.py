# Generated by Django 3.2.2 on 2021-05-13 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0002_banner_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description2', models.CharField(max_length=200)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecomApp.about_name')),
            ],
        ),
    ]
