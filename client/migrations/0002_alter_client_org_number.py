# Generated by Django 4.0 on 2021-12-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='org_number',
            field=models.CharField(blank=True, max_length=255, verbose_name="organisation's number"),
        ),
    ]