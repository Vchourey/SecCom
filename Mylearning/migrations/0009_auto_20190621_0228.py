# Generated by Django 2.1.2 on 2019-06-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mylearning', '0008_auto_20190621_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_form',
            name='EmailStu',
            field=models.EmailField(default='vijay@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='reg_form',
            name='TextArea',
            field=models.TextField(default='no comments'),
        ),
    ]