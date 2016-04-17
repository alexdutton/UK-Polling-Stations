# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollingstations', '0006_residentialaddress_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pollingdistrict',
            unique_together=set([('council', 'internal_council_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='pollingstation',
            unique_together=set([('council', 'internal_council_id')]),
        ),
    ]
