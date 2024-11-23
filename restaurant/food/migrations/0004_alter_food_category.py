# Generated by Django 5.1.3 on 2024-11-23 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='food.foodcategory', verbose_name='Раздел меню'),
        ),
    ]