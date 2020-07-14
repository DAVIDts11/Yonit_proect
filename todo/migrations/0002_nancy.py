# Generated by Django 3.0.4 on 2020-07-13 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('dateCompleted', models.DateField(blank=True, null=True)),
                ('mealName', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('Ingredients', models.CharField(max_length=70)),
                ('HasItamarTasted', models.BooleanField(default=False)),
                ('Recipe', models.CharField(max_length=70)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
