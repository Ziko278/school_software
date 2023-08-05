# Generated by Django 4.2.1 on 2023-07-28 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resource', '0001_initial'),
        ('school_setting', '0001_initial'),
        ('student', '0001_initial'),
        ('attendance', '0001_initial'),
        ('academic', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsubjectattendancemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='studentsubjectattendancemodel',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.classesmodel'),
        ),
        migrations.AddField(
            model_name='studentsubjectattendancemodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.subjectsmodel'),
        ),
        migrations.AddField(
            model_name='studentsubjectattendancemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentclassattendancerecordmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='studentclassattendancemodel',
            name='class_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.classsectionmodel'),
        ),
        migrations.AddField(
            model_name='studentclassattendancemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='studentclassattendancemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='studentclassattendancemodel',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.classesmodel'),
        ),
        migrations.AddField(
            model_name='studentattendancemodel',
            name='class_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.classsectionmodel'),
        ),
        migrations.AddField(
            model_name='studentattendancemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='studentattendancemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='studentattendancemodel',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.classesmodel'),
        ),
        migrations.AddField(
            model_name='studentattendancemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='class_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.classsectionmodel'),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.classesmodel'),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.subjectsmodel'),
        ),
        migrations.AddField(
            model_name='staffclassattendancemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='staffattendancemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='staffattendancemodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='staffattendancemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='holidaymodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='holidaymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventdaymodel',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.eventmodel'),
        ),
        migrations.AddField(
            model_name='eventdaymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.eventdaymodel'),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='parent',
            field=models.ManyToManyField(blank=True, to='student.parentsmodel'),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='staff',
            field=models.ManyToManyField(blank=True, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='student',
            field=models.ManyToManyField(blank=True, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='eventattendancemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancesettingmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
