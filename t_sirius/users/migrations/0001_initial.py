# Generated by Django 5.1.3 on 2024-12-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('user_address', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]