# Generated by Django 3.1.4 on 2022-03-13 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20220307_0834'),
        ('warehouse', '0004_auto_20220313_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
    ]
