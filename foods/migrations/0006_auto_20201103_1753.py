# Generated by Django 3.0.4 on 2020-11-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_auto_20201103_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtype',
            name='add_date',
            field=models.DateField(verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='exp_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='opened_date',
            field=models.DateField(blank=True, null=True, verbose_name='opened date'),
        ),
    ]