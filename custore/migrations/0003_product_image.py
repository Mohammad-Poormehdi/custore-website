# Generated by Django 4.1.5 on 2023-02-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custore', '0002_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/'),
        ),
    ]
