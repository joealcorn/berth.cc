# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('''
CREATE OR REPLACE FUNCTION job_number_auto()
    RETURNS trigger AS $$
DECLARE
    _rel_id constant int := 'job_job'::regclass::int;
    _prj_id int;
BEGIN
    _prj_id = NEW.project_id;

    -- Obtain an advisory lock on this table/group.
    PERFORM pg_advisory_xact_lock(_rel_id, _prj_id);

    SELECT  COALESCE(MAX(number) + 1, 1)
    INTO    NEW.number
    FROM    job_job
    WHERE   project_id = NEW.project_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql STRICT;

CREATE TRIGGER job_number_auto
    BEFORE INSERT ON job_job
    FOR EACH ROW
    EXECUTE PROCEDURE job_number_auto();

        ''', reverse_sql='''
DROP TRIGGER IF EXISTS job_number_auto on job_job;
DROP FUNCTION IF EXISTS job_number_auto();
        ''')
    ]
