# Generated by Django 2.1.2 on 2019-06-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mylearning', '0003_auto_20190617_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FiestName', models.CharField(max_length=50)),
                ('LasteName', models.CharField(max_length=50)),
                ('EmailStu', models.EmailField(max_length=254)),
                ('TextArea', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='interview_qa',
            name='question_num',
            field=models.IntegerField(unique=True),
        ),
    ]