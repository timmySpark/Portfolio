# Generated by Django 4.0.4 on 2022-07-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon_name',
            field=models.CharField(max_length=45),
        ),
    ]