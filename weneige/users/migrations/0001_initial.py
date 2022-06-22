# Generated by Django 4.0.5 on 2022-06-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=60)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
