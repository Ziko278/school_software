# Generated by Django 4.2.1 on 2023-07-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_lessonnotemodel_lessondocumentmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessondocumentmodel',
            name='class_section',
        ),
        migrations.RemoveField(
            model_name='lessonnotemodel',
            name='class_section',
        ),
        migrations.AlterField(
            model_name='lessondocumentmodel',
            name='student_class',
            field=models.ManyToManyField(blank=True, to='academic.classsectioninfomodel'),
        ),
        migrations.AlterField(
            model_name='lessonnotemodel',
            name='student_class',
            field=models.ManyToManyField(blank=True, to='academic.classsectioninfomodel'),
        ),
    ]
