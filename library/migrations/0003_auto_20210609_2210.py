# Generated by Django 3.2.4 on 2021-06-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210609_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
