# Generated by Django 4.0.5 on 2023-06-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_group_is_subgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='has_subgroup',
            field=models.BooleanField(default=False),
        ),
    ]
