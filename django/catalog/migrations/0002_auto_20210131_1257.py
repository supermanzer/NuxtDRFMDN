# Generated by Django 3.1.5 on 2021-01-31 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.URLField(blank=True, help_text='A URL to an image for this book', null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='instances', to='catalog.book'),
        ),
    ]
