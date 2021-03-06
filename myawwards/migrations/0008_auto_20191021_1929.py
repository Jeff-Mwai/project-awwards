# Generated by Django 2.2.6 on 2019-10-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0007_auto_20191021_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='content_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='design_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
