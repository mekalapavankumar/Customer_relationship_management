# Generated by Django 4.2.1 on 2023-07-02 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0007_course_student_delete_student_deleted_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
