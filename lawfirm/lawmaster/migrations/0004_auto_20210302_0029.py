# Generated by Django 2.1.15 on 2021-03-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawmaster', '0003_auto_20210302_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyers',
            name='bio',
            field=models.TextField(),
        ),
    ]
