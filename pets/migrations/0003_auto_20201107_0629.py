# Generated by Django 3.1.2 on 2020-11-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201025_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]