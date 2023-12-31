# Generated by Django 4.2.1 on 2023-07-28 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human_resource', '0001_initial'),
        ('school_setting', '0001_initial'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffloanmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='staffdeductionmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='staffdeductionmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='staffbonusmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='staffbonusmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='payrollmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='payrollmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='outstandingfeemodel',
            name='fee_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemastermodel'),
        ),
        migrations.AddField(
            model_name='outstandingfeemodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
    ]
