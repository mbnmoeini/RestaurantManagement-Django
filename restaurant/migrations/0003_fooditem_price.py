# Generated by Django 4.1 on 2022-08-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_fooditem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=9.99, max_digits=10),
            preserve_default=False,
        ),
    ]
