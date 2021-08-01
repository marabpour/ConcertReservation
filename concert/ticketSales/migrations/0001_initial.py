# Generated by Django 3.1.7 on 2021-07-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='concertModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('SingerName', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('test', models.CharField(max_length=10, null=True)),
                ('Poster', models.ImageField(null=True, upload_to='ConcertImages/')),
            ],
        ),
        migrations.CreateModel(
            name='locationModel',
            fields=[
                ('IdNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(default='تهران-برج میلاد', max_length=500)),
                ('Phone', models.CharField(max_length=11, null=True)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('ProfileImage', models.ImageField(upload_to='ProfileImages/')),
                ('Gender', models.IntegerField(choices=[('Man', 'مرد'), ('Woman', 'زن')])),
            ],
        ),
        migrations.CreateModel(
            name='timeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDateTime', models.DateTimeField()),
                ('Seats', models.IntegerField()),
                ('Status', models.IntegerField(choices=[('Start', 'فروش بلیط شروع شده است'), ('End', 'فروش بلیط تمام شده است'), ('Cancel', 'این سانس کنسل شده است'), ('Sales', 'در حال فروش بلیط')])),
                ('concertModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.concertmodel')),
                ('locationModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.locationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ticketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketImage', models.ImageField(upload_to='TicketImages/')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('ProfileModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.profilemodel')),
                ('timeModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.timemodel')),
            ],
        ),
    ]