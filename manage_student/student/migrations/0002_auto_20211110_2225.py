# Generated by Django 3.2.9 on 2021-11-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='frist_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
