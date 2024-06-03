# Generated by Django 5.0.3 on 2024-06-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0003_alter_users_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
