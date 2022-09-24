# Generated by Django 3.2.5 on 2022-09-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benedict_option', '0004_auto_20220923_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group_invitation',
        ),
        migrations.AddField(
            model_name='user',
            name='group_invitation',
            field=models.ManyToManyField(blank=True, related_name='group_invites', to='benedict_option.Group_Invite'),
        ),
    ]