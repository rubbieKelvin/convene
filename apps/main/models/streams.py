from uuid import uuid4
from django.db import models

class Stream(models.Model):
    def _default_content():
        return {'type': 'doc', 'content': []}

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    author = models.ForeignKey('main.User', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    content = models.JSONField(default=_default_content)
    is_deleted = models.BooleanField(default=False)
    scheduled_for = models.DateTimeField(default=None, null=True, blank=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)


class StreamComment(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    author = models.ForeignKey('main.User', on_delete=models.DO_NOTHING),
    date_commented = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, null=False)
    stream = models.ForeignKey('main.Stream', related_name='comments', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)