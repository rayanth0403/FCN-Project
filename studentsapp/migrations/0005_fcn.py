# Generated by Django 3.2.6 on 2022-04-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0004_auto_20170622_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='FCN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbank', models.CharField(max_length=20)),
                ('cinvestor', models.CharField(max_length=20)),
                ('ctradingDay', models.DateField()),
                ('creleaseDay', models.DateField()),
                ('cexpiryDay', models.DateField()),
                ('cransomDay', models.DateField()),
                ('cfinalEvaluation', models.DateField()),
                ('corder', models.BooleanField(default=True)),
                ('camount', models.FloatField()),
                ('crate', models.FloatField()),
                ('cstock1', models.CharField(max_length=20)),
                ('cstock1KOPrice', models.FloatField()),
                ('cstock1Exist', models.BooleanField(default=True)),
                ('cstock1StartPrice', models.FloatField()),
                ('cstock1TranformPrice', models.FloatField()),
                ('cstock2', models.CharField(blank=True, max_length=20)),
                ('cstock2KOPrice', models.FloatField(null=True)),
                ('cstock2Exist', models.BooleanField(default=True)),
                ('cstock2StartPrice', models.FloatField(null=True)),
                ('cstock2TranformPrice', models.FloatField(null=True)),
                ('cstock3', models.CharField(blank=True, max_length=20)),
                ('cstock3KOPrice', models.FloatField(null=True)),
                ('cstock3Exist', models.BooleanField(default=True)),
                ('cstock3StartPrice', models.FloatField(null=True)),
                ('cstock3TranformPrice', models.FloatField(null=True)),
                ('cstock4', models.CharField(blank=True, max_length=20)),
                ('cstock4KOPrice', models.FloatField(null=True)),
                ('cstock4Exist', models.BooleanField(default=True)),
                ('cstock4StartPrice', models.FloatField(null=True)),
                ('cstock4TranformPrice', models.FloatField(null=True)),
                ('ccurrency', models.CharField(max_length=20)),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('cPhone', models.CharField(blank=True, default='', max_length=50)),
                ('cAddr', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]