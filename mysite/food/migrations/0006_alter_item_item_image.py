# Generated by Django 4.0.4 on 2022-05-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://c8.alamy.com/comp/B3C2XG/taking-a-slice-of-pizza-B3C2XG.jpg', max_length=500),
        ),
    ]
