# Generated by Django 3.0.4 on 2020-03-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20200322_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labpost',
            name='postbody',
            field=models.TextField(null=True),
        ),
    ]