# Generated by Django 3.1.5 on 2021-01-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_info',
            field=models.CharField(max_length=200, null=True, verbose_name='Информация о факультете'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_name',
            field=models.CharField(max_length=10, null=True, verbose_name='Название факультета'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_number',
            field=models.IntegerField(null=True, verbose_name='Номер факультета'),
        ),
    ]
