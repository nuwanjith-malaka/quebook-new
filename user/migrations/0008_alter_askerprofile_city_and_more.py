# Generated by Django 4.0 on 2022-01-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_askerprofile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askerprofile',
            name='city',
            field=models.CharField(default='sample city', max_length=20),
        ),
        migrations.AlterField(
            model_name='askerprofile',
            name='first_name',
            field=models.CharField(default='john', max_length=20),
        ),
        migrations.AlterField(
            model_name='askerprofile',
            name='grade',
            field=models.CharField(choices=[('10', '10'), ('11', '11')], default='10', max_length=2),
        ),
        migrations.AlterField(
            model_name='askerprofile',
            name='last_name',
            field=models.CharField(default='doe', max_length=20),
        ),
        migrations.AlterField(
            model_name='askerprofile',
            name='school',
            field=models.CharField(default='sample shool', max_length=50),
        ),
    ]
