# Generated by Django 3.1.7 on 2021-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EngWS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chapter', models.CharField(max_length=300)),
                ('EngWSFile', models.FileField(upload_to='EngWS')),
            ],
        ),
    ]
