# Generated by Django 4.0.4 on 2022-05-09 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-date_added',)},
        ),
    ]