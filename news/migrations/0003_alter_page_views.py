# Generated by Django 4.2 on 2024-09-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
