# Generated by Django 5.1.1 on 2024-09-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('education', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('wechat_id', models.CharField(max_length=100)),
                ('initial_notes', models.TextField()),
            ],
        ),
    ]
