# Generated by Django 4.1.3 on 2022-12-06 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_autor_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cteated_on',
            new_name='created_on',
        ),
    ]
