# Generated by Django 2.1.15 on 2021-03-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Lawyers')),
                ('lawSchool', models.CharField(max_length=150)),
                ('recognisedSince', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('languages', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('biography', models.DateField()),
            ],
        ),
    ]
