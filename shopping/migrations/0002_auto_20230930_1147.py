# Generated by Django 2.2.2 on 2023-09-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Philips', 'Philips'), ('Puma', 'Puma'), ('Elica', 'Elica'), ('Sugar', 'Sugar'), ('Amazon Books', 'Amazon Books')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Kitchen Appliances', 'Kitchen Appliances'), ('Beauty Products', 'Beauty Products'), ('Books', 'Books')], max_length=50),
        ),
    ]
