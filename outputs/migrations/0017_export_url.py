# Generated by Django 4.2.3 on 2023-08-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0016_alter_export_creator_alter_export_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='url',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]