# Generated by Django 3.0.7 on 2020-06-24 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orders',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
    ]
