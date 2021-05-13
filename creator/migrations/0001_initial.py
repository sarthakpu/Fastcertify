# Generated by Django 3.1.7 on 2021-03-16 09:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('upload', '0002_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='emailonly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lines', models.IntegerField()),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=400)),
                ('cc', models.CharField(blank=True, max_length=100, null=True)),
                ('bcc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='filemaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventYear', models.IntegerField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028')], default=2021, null=True, verbose_name='year of the event')),
                ('filed', models.DateTimeField(auto_now_add=True)),
                ('xaxis', models.IntegerField(default=0, verbose_name='Name x-axis ')),
                ('yaxis', models.IntegerField(default=0, verbose_name='Name y-axis')),
                ('thickness', models.PositiveIntegerField(default=2, verbose_name='thickness for the name')),
                ('date', models.CharField(default=datetime.date(2021, 3, 16), max_length=100)),
                ('date_xaxis', models.IntegerField(default=0, verbose_name='Date x-axis')),
                ('date_yaxis', models.IntegerField(default=0, verbose_name='Date y-axis')),
                ('datethick', models.IntegerField(verbose_name='thickness for the date')),
                ('eventName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='upload.events', verbose_name='event name')),
            ],
        ),
    ]
