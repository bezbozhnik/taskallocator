# Generated by Django 4.0.5 on 2023-05-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_task_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_table',
            field=models.IntegerField(null=True),
        ),
    ]
