# Generated by Django 3.0.5 on 2020-12-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adpro', '0003_auto_20201202_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_superadmin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]