# Generated by Django 3.0.4 on 2020-11-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_foodtype_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtype',
            name='exp_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='foodtype',
            name='opened_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='opened date'),
        ),
    ]
