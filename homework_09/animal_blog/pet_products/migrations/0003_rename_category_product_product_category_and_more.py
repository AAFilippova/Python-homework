# Generated by Django 5.1 on 2024-08-29 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalblog_app', '0002_author_article'),
        ('pet_products', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
        migrations.AddField(
            model_name='product',
            name='animal_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='animalblog_app.animalcategory'),
            preserve_default=False,
        ),
    ]
