# Generated by Django 3.1 on 2022-05-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20220525_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='is_public',
            field=models.BooleanField(default=1),
        ),
    ]
