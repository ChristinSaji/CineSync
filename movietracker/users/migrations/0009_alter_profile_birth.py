# Generated by Django 3.2.5 on 2023-01-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20211229_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
