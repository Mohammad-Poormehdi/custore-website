# Generated by Django 4.1.5 on 2023-03-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custore', '0006_customer_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
