# Generated by Django 3.2.4 on 2021-06-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
