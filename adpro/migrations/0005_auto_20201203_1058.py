# Generated by Django 3.0.5 on 2020-12-03 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adpro', '0004_auto_20201202_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_user',
        ),
    ]
