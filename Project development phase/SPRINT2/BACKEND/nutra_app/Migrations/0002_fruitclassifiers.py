# Generated by Django 4.1.3 on 2022-11-09 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nutra_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('nutra_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitClassifier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=nutra_app.models.upload_location)),
                ('model_predicted_output', models.CharField(blank=True, default='', max_length=255)),
                ('human_predicted_output', models.CharField(blank=True, default='', max_length=255)),
                ('is_predicted_by_model_and_human_are_same', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, default='', max_length=255)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
