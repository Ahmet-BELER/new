# Generated by Django 4.1 on 2022-10-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
