# Generated by Django 4.2.1 on 2023-07-28 04:24

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
            name='SchoolAcademicInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')], max_length=10)),
                ('next_resumption_date', models.DateField(blank=True, null=True)),
                ('closing_date', models.DateField(blank=True, null=True)),
                ('current_resumption_date', models.DateField(blank=True, null=True)),
                ('no_of_students', models.FloatField(blank=True, null=True)),
                ('no_of_staff', models.FloatField(blank=True, null=True)),
                ('no_of_parents', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolGeneralInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('short_name', models.CharField(max_length=50)),
                ('school_type', models.CharField(choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')], max_length=200)),
                ('logo', models.FileField(blank=True, upload_to='images/logo')),
                ('mobile_1', models.CharField(max_length=20)),
                ('mobile_2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('separate_school_section', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')], max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('delimeter', models.CharField(choices=[('-', '-'), ('/', '/')], max_length=1)),
                ('status', models.CharField(choices=[('a', 'ACTIVE'), ('p', 'PAST'), ('n', 'NEXT')], max_length=1)),
                ('type', models.CharField(choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_setting.schoolacademicinfomodel')),
                ('general_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.schoolgeneralinfomodel')),
            ],
        ),
        migrations.AddField(
            model_name='schoolacademicinfomodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
    ]
