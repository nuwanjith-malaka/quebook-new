# Generated by Django 4.0 on 2022-01-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_askerprofile_grade_askerprofile_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='askerprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='askerprofile',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]