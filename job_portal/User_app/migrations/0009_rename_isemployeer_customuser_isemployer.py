# Generated by Django 5.1.1 on 2024-09-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0008_alter_customuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='isEmployeer',
            new_name='isEmployer',
        ),
    ]
