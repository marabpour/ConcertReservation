# Generated by Django 3.1.7 on 2021-07-31 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210731_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='Gender',
            field=models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربری'),
        ),
    ]
