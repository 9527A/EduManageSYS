# Generated by Django 2.2.1 on 2019-05-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_selection', '0003_auto_20190503_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, to='course_selection.Course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
