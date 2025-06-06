# Generated by Django 4.1.2 on 2023-03-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_profile_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='recommended_by',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
