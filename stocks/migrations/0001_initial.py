# Generated by Django 2.2.19 on 2021-03-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('published', models.CharField(max_length=70)),
                ('cashtag', models.CharField(max_length=70)),
                ('name', models.CharField(max_length=70)),
                ('full_name', models.CharField(max_length=70)),
                ('stock_price', models.CharField(max_length=70)),
                ('price_change_rm', models.CharField(max_length=70)),
                ('price_change_pct', models.CharField(max_length=70)),
                ('volume', models.CharField(max_length=70)),
                ('marketcap', models.CharField(max_length=70)),
                ('board', models.CharField(blank=True, max_length=70)),
                ('sector', models.CharField(blank=True, max_length=70)),
                ('is_shariah', models.CharField(max_length=70)),
            ],
        ),
    ]
