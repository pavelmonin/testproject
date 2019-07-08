# Generated by Django 2.2.2 on 2019-06-26 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
