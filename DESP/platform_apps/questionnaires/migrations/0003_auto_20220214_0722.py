# Generated by Django 3.2.4 on 2022-02-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='indicator',
            name='app_indicator_parent_question_null',
        ),
        migrations.AlterField(
            model_name='indicator',
            name='question',
            field=models.TextField(blank=True, null=True, verbose_name='指向问题'),
        ),
    ]
