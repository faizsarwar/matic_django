# Generated by Django 4.0.4 on 2022-05-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_blog_card_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='classes_per_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='durantion_in_months',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='homework',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='learning_targets',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='pre_requisites',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='price_per_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='scheduling',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='total_duration_in_minutes',
            field=models.IntegerField(null=True),
        ),
    ]
