# Generated by Django 3.2.4 on 2021-11-15 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20211115_1444'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('id', 'order', 'title', 'stem')},
        ),
    ]
