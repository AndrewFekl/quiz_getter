# Generated by Django 4.0.4 on 2022-05-10 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='hint',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='created',
            new_name='created_at',
        ),
    ]