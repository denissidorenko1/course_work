# Generated by Django 3.1.5 on 2021-01-15 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_work', '0003_auto_20210115_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='Faculty_FK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_work.faculty'),
        ),
    ]
