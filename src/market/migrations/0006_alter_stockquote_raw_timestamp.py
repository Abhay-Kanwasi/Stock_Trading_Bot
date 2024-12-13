# Generated by Django 5.1.4 on 2024-12-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_stockquote_raw_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockquote',
            name='raw_timestamp',
            field=models.CharField(blank=True, help_text='Non transformed timestamp string or int or float', max_length=120, null=True),
        ),
    ]
