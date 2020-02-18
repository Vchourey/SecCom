# Generated by Django 2.1.2 on 2020-01-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=150)),
                ('address_line', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('contact_Person', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_date', models.DateTimeField(auto_created=True)),
                ('enquiry_number', models.IntegerField(unique_for_date=True)),
                ('enquire_name', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address_location', models.TextField()),
                ('Service_Product', models.CharField(max_length=200)),
                ('Requirements', models.TextField()),
                ('Image', models.ImageField(upload_to='')),
                ('File', models.FileField(upload_to='')),
            ],
        ),
    ]