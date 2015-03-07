from django.db import models


class Model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def _do_insert(self, manager, *a, **kw):
        '''
        This is required as part of the `insert...returning` hack.
        All it does is replaces the base manager in the call
        with the specified manager, which does the rest of the work.
        '''
        if getattr(self.__class__.objects, 'insert_returning', False):
            manager = self.__class__.objects
        return super(Model, self)._do_insert(manager, *a, **kw)

    class Meta:
        abstract = True
