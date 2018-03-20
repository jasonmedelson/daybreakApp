# Generated by Django 2.0 on 2018-03-20 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0003_auto_20180316_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='youtubeLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.CharField(max_length=20)),
                ('influencer', models.CharField(max_length=50)),
                ('videourl', models.CharField(max_length=200)),
                ('channelurl', models.CharField(max_length=200)),
                ('views', models.IntegerField()),
                ('viewsdate', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]