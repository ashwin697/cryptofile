# Generated by Django 3.0.7 on 2020-10-19 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Decrypt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=70)),
                ('dfile', models.FileField(upload_to='decrypt')),
                ('password', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Encrypt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='encrypt')),
                ('password', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fpath', models.FilePathField(path='media/encrypted_file')),
                ('filename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cf.Encrypt')),
            ],
        ),
        migrations.CreateModel(
            name='DecryptedPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fpath', models.FilePathField(path='media/decrypted')),
                ('filename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cf.Decrypt')),
            ],
        ),
    ]
