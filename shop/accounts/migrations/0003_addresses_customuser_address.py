# Generated by Django 5.1.6 on 2025-03-04 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(max_length=100)),
                ('room', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('code', models.IntegerField()),
                ('entrance', models.IntegerField()),
                ('comment', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.addresses'),
        ),
    ]
