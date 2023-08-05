# Generated by Django 4.2.1 on 2023-07-28 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.IntegerField()),
                ('reference', models.CharField(max_length=20)),
                ('default_password', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')], max_length=10, null=True)),
                ('parent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_account', to='student.parentsmodel')),
                ('staff', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='human_resource.staffmodel')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_account', to='student.studentsmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
