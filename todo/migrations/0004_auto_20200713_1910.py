# Generated by Django 3.0.4 on 2020-07-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_nancy_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nancy',
            name='imagefile',
            field=models.ImageField(blank=True, null=True, upload_to='nancy/images'),
        ),
    ]
