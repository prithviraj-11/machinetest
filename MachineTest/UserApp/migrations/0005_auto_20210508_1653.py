# Generated by Django 3.1.7 on 2021-05-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_auto_20210508_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
