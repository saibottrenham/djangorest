# Generated by Django 3.1.7 on 2021-12-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('ratings', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
