# Generated by Django 4.2.1 on 2023-07-28 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0002_initial'),
        ('school_setting', '0001_initial'),
        ('student', '0001_initial'),
        ('academic', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outstandingfeemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='onlinepaymentmodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='online_payment_method_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='onlinepaymentmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomesourcemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='income_source_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomesourcemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.incomecategorymodel'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='session',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.incomesourcemodel'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='income_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomecategorymodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='income_category_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incomecategorymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='financesettingmodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='finance_setting_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='financesettingmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feereminderrecordmodel',
            name='reminder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feeremindermodel'),
        ),
        migrations.AddField(
            model_name='feereminderrecordmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='feereminderrecordmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feeremindermodel',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemodel'),
        ),
        migrations.AddField(
            model_name='feeremindermodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_reminder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feeremindermodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feerecordmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='feepenaltymodel',
            name='fee_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemastermodel'),
        ),
        migrations.AddField(
            model_name='feepenaltymodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_penalty_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feepenaltymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feepaymentsummarymodel',
            name='fees',
            field=models.ManyToManyField(related_name='payment_summary', to='finance.feepaymentmodel'),
        ),
        migrations.AddField(
            model_name='feepaymentsummarymodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='feepaymentsummarymodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='feepaymentsummarymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feepaymentmodel',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemastermodel'),
        ),
        migrations.AddField(
            model_name='feepaymentmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='feepaymentmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='feepaymentmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='class_section',
            field=models.ManyToManyField(blank=True, to='academic.classsectionmodel'),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemodel'),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feegroupmodel'),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='student_class',
            field=models.ManyToManyField(blank=True, to='academic.classesmodel'),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_master_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feemastermodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feegroupmodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_group_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feegroupmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feediscountmodel',
            name='fee_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.feemastermodel'),
        ),
        migrations.AddField(
            model_name='feediscountmodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_discount_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feediscountmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feediscountgroupmodel',
            name='discounts',
            field=models.ManyToManyField(blank=True, to='finance.feediscountmodel'),
        ),
        migrations.AddField(
            model_name='feediscountgroupmodel',
            name='students',
            field=models.ManyToManyField(blank=True, to='student.studentsmodel'),
        ),
        migrations.AddField(
            model_name='feediscountgroupmodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_discount_group_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feediscountgroupmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensetypemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_types', to='finance.expensecategorymodel'),
        ),
        migrations.AddField(
            model_name='expensetypemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_type_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensetypemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.expensecategorymodel'),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='expense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.expensetypemodel'),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='session',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensecategorymodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_category_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expensecategorymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budgetmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.expensecategorymodel'),
        ),
        migrations.AddField(
            model_name='budgetmodel',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_setting.sessionmodel'),
        ),
        migrations.AddConstraint(
            model_name='incomesourcemodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_income_source_type_combo', violation_error_message='Income Source Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='incomemodel',
            constraint=models.UniqueConstraint(fields=('invoice_number', 'type'), name='unique_income_invoice_type_combo', violation_error_message='Income Source Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='incomecategorymodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_income_category_type_combo', violation_error_message='Income Category Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='feemodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_fee_name_type_combo', violation_error_message='Fee Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='feemastermodel',
            constraint=models.UniqueConstraint(fields=('fee', 'group', 'type'), name='unique_fee_master_type_combo', violation_error_message='Fee Grouping Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='feegroupmodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_fee_group_type_combo', violation_error_message='Fee Group Already Exists'),
        ),
        migrations.AddConstraint(
            model_name='expensecategorymodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_expense_source_type_combo', violation_error_message='Expense Category Already Exists'),
        ),
    ]
