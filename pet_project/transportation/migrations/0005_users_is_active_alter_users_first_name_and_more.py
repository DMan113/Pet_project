# Generated by Django 5.0.3 on 2024-06-03 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_remove_users_is_active_users_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password_hash',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\\d!@#$%^&*(),.?":{}|<>]{8,}$', message='Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.')]),
        ),
    ]