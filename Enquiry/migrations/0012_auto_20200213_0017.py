# Generated by Django 2.2.9 on 2020-02-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0011_auto_20200213_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='file',
            field=models.FileField(blank=True, upload_to='Enquiry/media/files/'),
        ),
    ]
