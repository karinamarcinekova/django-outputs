# Generated by Django 2.2.9 on 2020-09-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0005_change_column_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='send_separately',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='send_separately',
            field=models.BooleanField(default=False),
        ),
    ]
