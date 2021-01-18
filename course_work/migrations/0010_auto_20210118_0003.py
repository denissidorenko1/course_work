# Generated by Django 3.1.5 on 2021-01-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_work', '0009_auto_20210117_0548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='lecturer_name_surname',
            new_name='teacher_name_surname',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='stop_date',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='grading_method',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='practice_name_surname',
        ),
        migrations.AddField(
            model_name='subject',
            name='Semester_number',
            field=models.IntegerField(default=0, verbose_name='Номер семестра'),
        ),
        migrations.AddField(
            model_name='subject',
            name='Student_FIO',
            field=models.CharField(default='Пупкин Вася Станиславович', max_length=50, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='subject',
            name='grade',
            field=models.CharField(max_length=30, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='TeachingPlan_id',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер учебного плана'),
        ),
    ]
