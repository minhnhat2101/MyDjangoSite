# Generated by Django 4.2.2 on 2023-06-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcustomer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]