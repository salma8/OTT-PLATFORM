# Generated by Django 5.0.6 on 2024-05-30 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_password_alter_movie_actors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium')], max_length=15, null='True')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10, null='True')),
                ('duration_months', models.IntegerField(null='True')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Plan',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(max_length=254, null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='FirstName',
            field=models.CharField(max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='LastName',
            field=models.CharField(max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Mobile',
            field=models.CharField(max_length=10, null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=16, null='True'),
        ),
        migrations.AddField(
            model_name='customer',
            name='subscription',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='app.subscription'),
            preserve_default='True',
        ),
    ]
