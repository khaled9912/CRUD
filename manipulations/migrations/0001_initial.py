# Generated by Django 4.0 on 2022-01-02 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('phone', models.CharField(max_length=64, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('price', models.FloatField(max_length=23, null=True)),
                ('category', models.CharField(choices=[('In Door', 'In Door'), ('Out Door', 'Out Door')], max_length=64)),
                ('description', models.CharField(max_length=64, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='manipulations.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=64)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manipulations.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manipulations.product')),
            ],
        ),
    ]
