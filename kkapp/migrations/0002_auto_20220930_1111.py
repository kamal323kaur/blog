# Generated by Django 3.0 on 2022-09-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kkapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email_id',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
