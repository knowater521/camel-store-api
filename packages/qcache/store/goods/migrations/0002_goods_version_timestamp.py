# Generated by Django 2.2.7 on 2019-12-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='version_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]