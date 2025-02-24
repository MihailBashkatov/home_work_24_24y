# Generated by Django 5.1.4 on 2024-12-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150, verbose_name='Country')),
                ('inn', models.CharField(max_length=20, verbose_name='INN')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['country'],
            },
        ),
    ]
