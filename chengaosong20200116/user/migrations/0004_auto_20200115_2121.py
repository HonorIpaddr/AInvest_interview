# Generated by Django 3.0.1 on 2020-01-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200115_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_pay',
            field=models.BooleanField(default=False),
        ),
    ]