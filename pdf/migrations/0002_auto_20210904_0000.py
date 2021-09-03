# Generated by Django 3.2.5 on 2021-09-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='about',
            new_name='achievements',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='university',
            new_name='cgpa',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='previousWork',
            new_name='extracurr',
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='passyear',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='post',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
    ]