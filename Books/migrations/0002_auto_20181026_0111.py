# Generated by Django 2.1.2 on 2018-10-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donner',
            name='member_id',
            field=models.IntegerField(),
        ),
    ]
