# Generated by Django 2.1.2 on 2020-01-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeyard', '0002_auto_20190630_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(unique=True)),
                ('service_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('service_had', models.CharField(max_length=150)),
                ('contact', models.IntegerField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('contact_Person', models.CharField(max_length=100)),
            ],
        ),
    ]
