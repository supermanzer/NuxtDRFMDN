# Generated by Django 3.1.5 on 2021-03-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210221_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedcopy',
            name='late_fee',
        ),
        migrations.AddField(
            model_name='borrowedcopy',
            name='assessed_late_fee',
            field=models.FloatField(help_text='Late fee assessed (if any)', null=True, verbose_name='Late Fee'),
        ),
    ]