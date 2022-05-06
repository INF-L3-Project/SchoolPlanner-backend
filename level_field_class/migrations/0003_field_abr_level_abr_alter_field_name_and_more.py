# Generated by Django 4.0.4 on 2022-05-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_field_class', '0002_rename_class_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='abr',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='abr',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
