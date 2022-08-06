from django.contrib import admin
from .models.user import User
from .models.space import Space, SpaceInvites, SpaceMembership
from .models.room import Room, RoomMembership
from .models.streams import Stream, StreamComment

admin.site.register([
    User,
    Space,
    SpaceMembership,
    SpaceInvites,
    Room,
    RoomMembership,
    Stream,
    StreamComment])
