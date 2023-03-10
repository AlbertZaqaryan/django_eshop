# Generated by Django 4.1.7 on 2023-02-24 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_addition_bool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category products name')),
                ('img', models.ImageField(upload_to='media', verbose_name='Category products image')),
                ('price', models.IntegerField(verbose_name='Category product price')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categ_prod', to='main.subcategory')),
            ],
            options={
                'verbose_name': 'Category_Product',
                'verbose_name_plural': 'Category_Products',
            },
        ),
    ]
