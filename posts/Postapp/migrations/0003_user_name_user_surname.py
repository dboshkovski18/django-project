# Generated by Django 4.0.5 on 2022-06-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Postapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]