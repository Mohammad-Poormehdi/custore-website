# Generated by Django 4.1.5 on 2023-02-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='custore.category'),
        ),
    ]
