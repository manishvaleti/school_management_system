# Generated by Django 5.0.3 on 2024-04-23 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_system', '0006_superkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superkey',
            name='class_reg_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school_management_system.classregister'),
        ),
        migrations.AlterField(
            model_name='superkey',
            name='payment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school_management_system.payment'),
        ),
    ]