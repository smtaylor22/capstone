# Generated by Django 3.2.5 on 2022-09-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benedict_option', '0002_remove_group_invite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_invite',
            name='accepted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]