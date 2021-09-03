# Generated by Django 3.2.6 on 2021-09-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210902_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocery_item',
            old_name='date',
            new_name='item_date',
        ),
        migrations.RenameField(
            model_name='grocery_item',
            old_name='amount',
            new_name='item_quantity',
        ),
        migrations.RemoveField(
            model_name='grocery_item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='grocery_item',
            name='status',
        ),
        migrations.AddField(
            model_name='grocery_item',
            name='item_name',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='grocery_item',
            name='item_status',
            field=models.CharField(choices=[('0', 'PENDING'), ('1', 'BOUGHT'), ('2', 'NOT AVAILABLE')], default=0, max_length=100),
        ),
    ]