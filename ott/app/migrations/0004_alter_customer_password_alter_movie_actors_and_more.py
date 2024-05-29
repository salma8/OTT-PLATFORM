# Generated by Django 5.0.6 on 2024-05-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customer_plan_alter_customer_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]