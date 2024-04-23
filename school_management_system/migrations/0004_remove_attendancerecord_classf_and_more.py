# Generated by Django 5.0.3 on 2024-04-20 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_system', '0003_alter_student_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancerecord',
            name='classF',
        ),
        migrations.RemoveField(
            model_name='attendancerecord',
            name='student',
        ),
        migrations.AddField(
            model_name='class',
            name='class_time',
            field=models.TimeField(null=True),
        ),
        migrations.CreateModel(
            name='ClassRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='school_management_system.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='school_management_system.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceRecord',
        ),
    ]