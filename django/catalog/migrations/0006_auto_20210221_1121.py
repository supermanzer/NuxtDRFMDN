# Generated by Django 3.1.5 on 2021-02-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_borrowedcopy_late_fee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrowedcopy',
            options={'ordering': ('copy',), 'verbose_name': 'Checkout History', 'verbose_name_plural': 'Checkout History'},
        ),
        migrations.AlterField(
            model_name='borrowedcopy',
            name='date_checked_out',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrowedcopy',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrowedcopy',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
