# Generated by Django 5.0.3 on 2024-03-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=5)),
                ('affiliation', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('quote', models.CharField(max_length=255)),
            ],
        ),
    ]