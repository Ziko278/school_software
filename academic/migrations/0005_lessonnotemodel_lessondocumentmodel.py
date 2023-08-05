# Generated by Django 4.2.1 on 2023-07-31 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academic', '0004_alter_academicsettingmodel_head_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonNoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('class_section', models.ManyToManyField(blank=True, to='academic.classsectionmodel')),
                ('student_class', models.ManyToManyField(blank=True, to='academic.classesmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.subjectsmodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson_note_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonDocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('grant_access', models.BooleanField(default=False)),
                ('document', models.FileField(upload_to='')),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('class_section', models.ManyToManyField(blank=True, to='academic.classsectionmodel')),
                ('student_class', models.ManyToManyField(blank=True, to='academic.classesmodel')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.subjectsmodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson_document_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]