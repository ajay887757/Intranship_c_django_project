# Generated by Django 3.2.4 on 2022-02-11 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('androidapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applied',
            name='payment_date',
        ),
    ]
