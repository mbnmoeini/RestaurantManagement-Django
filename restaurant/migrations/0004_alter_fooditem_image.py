# Generated by Django 4.0.6 on 2022-08-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_fooditem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(upload_to='restaurant'),
        ),
    ]
