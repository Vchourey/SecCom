# Generated by Django 2.2.9 on 2020-02-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0012_auto_20200213_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='file',
            field=models.FileField(blank=True, upload_to='media/files/'),
        ),
    ]