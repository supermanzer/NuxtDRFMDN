# Generated by Django 3.1.5 on 2021-03-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210301_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedcopy',
            name='assessed_late_fee',
            field=models.FloatField(blank=True, help_text='Late fee assessed (if any)', null=True, verbose_name='Late Fee'),
        ),
    ]