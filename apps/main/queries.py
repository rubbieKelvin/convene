from django.db import models

from .models.user import User
from .models.room import Room
from .models.space import Space

def usersAll():
    """gets all users"""
    return User.objects.filter(is_active=True)

def spacesAll():
    """gets all spaces"""
    return Space.objects.filter(is_deleted=False)

def roomsAll():
    """all rooms"""
    return Room.objects.filter(is_deleted=False)

def singleRoom(space:Space|str, id:str) -> Room:
    """returns a single room"""
    return roomsAll().filter(space=space, id=id)

def mySpaces(user: str|User) -> models.QuerySet[Space]:
    """returns all the spaces where user is a member of"""
    return spacesAll().filter(memberships__member=user, suspended=False)

def getSpace(user: str|User, id:str) -> Space|None:
    """returns a space by id"""
    return mySpaces(user).filter(id=id).first()

def getMyRooms(user: str|User, space_id:str) -> models.QuerySet[Room]:
    """returns all the rooms for a space a user is in"""
    return roomsAll().filter(
        space=getSpace(user, space_id),
        memberships__member=user)

def getSpaceMembers(space: str|Space) -> models.QuerySet[User]:
    """returns all the users that is a member of the given space"""
    return usersAll().filter(memberships__space=space)

def getRoomMembers(space: str|Space, room:str|Room) -> models.QuerySet[Room]:
    """returns all the users that belong to the given room"""
    return usersAll().filter(
        rooms__room=room,
        memberships__space=space)