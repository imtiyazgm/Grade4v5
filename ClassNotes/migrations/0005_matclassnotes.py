# Generated by Django 3.1.7 on 2021-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassNotes', '0004_araclassnotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatClassNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chapter', models.CharField(max_length=300)),
                ('MatNotesFile', models.FileField(upload_to='Maths_Notes')),
            ],
        ),
    ]