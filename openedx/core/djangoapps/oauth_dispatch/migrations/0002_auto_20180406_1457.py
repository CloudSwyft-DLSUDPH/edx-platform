# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-06 18:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_auto_20171207_0259'),
        ('oauth_dispatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictedapplication',
            name='_allowed_scopes',
            field=models.TextField(default=b'profile enrollments:read grades:read read write email certificates:read', null=True),
        ),
        migrations.AddField(
            model_name='restrictedapplication',
            name='_org_associations',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
        migrations.AlterField(
            model_name='restrictedapplication',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restricted_application', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]
