# Generated by Django 2.1.15 on 2021-03-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawmaster', '0005_lawyers_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyers',
            name='name',
            field=models.CharField(default='No', max_length=150),
            preserve_default=False,
        ),
    ]