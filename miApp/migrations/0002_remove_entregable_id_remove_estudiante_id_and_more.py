# Generated by Django 4.0.4 on 2022-05-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='id',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='id',
        ),
        migrations.AlterField(
            model_name='entregable',
            name='nombre',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]