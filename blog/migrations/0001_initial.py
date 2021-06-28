# Generated by Django 3.0.7 on 2020-08-31 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=260)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
