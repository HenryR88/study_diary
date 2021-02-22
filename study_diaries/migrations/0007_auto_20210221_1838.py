# Generated by Django 3.1.6 on 2021-02-21 18:38

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('study_diaries', '0006_auto_20210220_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(blank=True, upload_to='study_diaries/media'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='file',
            field=smartfields.fields.FileField(blank=True, upload_to='study_diaries/media/'),
        ),
    ]
