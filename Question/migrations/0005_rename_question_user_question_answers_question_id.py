# Generated by Django 4.1.4 on 2023-01-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0004_rename_question_id_user_question_answers_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_question_answers',
            old_name='question',
            new_name='question_id',
        ),
    ]
