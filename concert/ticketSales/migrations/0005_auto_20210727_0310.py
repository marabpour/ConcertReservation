# Generated by Django 3.1.7 on 2021-07-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0004_auto_20210727_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concertmodel',
            name='length',
            field=models.CharField(max_length=100, verbose_name='مدت زمان'),
        ),
    ]