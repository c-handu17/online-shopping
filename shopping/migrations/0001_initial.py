# Generated by Django 2.2.2 on 2023-09-29 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('category', models.CharField(choices=[('electronics', 'Electronics'), ('clothing', 'Clothing'), ('kitchen appliances', 'Kitchen Appliances'), ('beauty products', 'Beauty Products'), ('books', 'Books')], max_length=50)),
                ('brand', models.CharField(choices=[('philips', 'Philips'), ('puma', 'Puma'), ('elica', 'Elica'), ('sugar', 'Sugar'), ('amazon books', 'Amazon Books')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shopping.User')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User')),
            ],
        ),
    ]
