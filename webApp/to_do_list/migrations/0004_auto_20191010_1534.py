# Generated by Django 2.2.6 on 2019-10-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0003_auto_20191009_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemli',
            name='deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='itemli',
            name='edit',
            field=models.BooleanField(default=0),
        ),
    ]
