# Generated by Django 3.2.5 on 2023-01-17 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20211229_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviestatus',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tracker.category'),
        ),
    ]
