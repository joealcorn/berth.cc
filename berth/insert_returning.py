'''
This file does most of the work of hacking `insert...returning`
support into the orm.

It's mostly an adaptation of this project
https://github.com/kanu/django-update-returning
'''

from django.db import connections
from django.db.models import sql
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from django.db.models.sql import InsertQuery
from django.db.models.sql.compiler import SQLInsertCompiler


class InsertReturningManager(Manager):
    insert_returning = True

    def get_queryset(self):
        return InsertReturningQuerySet(self.model, using=self._db)


class InsertReturningQuerySet(QuerySet):
    def _insert(self, objs, fields, return_id=False, raw=False, using=None):
        self._for_write = True
        if using is None:
            using = self.db
        query = InsertReturningQuery(self.model)
        query.insert_values(fields, objs, raw=raw)
        returned = query.get_compiler(using=using).execute_sql(return_id)
        returned = list(returned)

        obj = objs[0]
        for index, value in enumerate(returned[0][0]):
            field = obj._meta.fields[index]
            if field.rel is None:
                setattr(obj, field.name, value)

        if return_id:
            return obj.pk

    _insert.alters_data = True
    _insert.queryset_only = False


class InsertReturningQuery(InsertQuery):
    def get_compiler(self, using=None, connection=None):
        if using is None and connection is None:
            raise ValueError('Need either using or connection')
        if using:
            connection = connections[using]
        return SQLInsertReturningCompiler(self, connection, using)


class SQLInsertReturningCompiler(SQLInsertCompiler):
    def as_sql(self):
        sql, params = super(SQLInsertReturningCompiler, self).as_sql()[0]
        columns = self.get_columns(False)[0]
        sql = '%s RETURNING %s' % (sql.rstrip(), ', '.join(columns))
        return [sql, params]

    def execute_sql(self, result_type):
        return super(SQLInsertCompiler, self).execute_sql(result_type)
