from uuid import uuid4
from django.db import models

class Room(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    creator = models.ForeignKey('main.User', on_delete=models.CASCADE, related_name="created_rooms")
    space = models.ForeignKey('main.Space', on_delete=models.CASCADE, related_name="rooms")
    private = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'space'],
                condition=models.Q(is_deleted=False),
                name='%(app_label)s_%(class)s_one_name_per_space')
        ]

class RoomMembership(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    member = models.ForeignKey('main.User', on_delete=models.CASCADE, related_name="rooms")
    room = models.ForeignKey('main.Room', on_delete=models.CASCADE, related_name="memberships")