from django.db import models
from uuid import uuid4

class Space(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=2000, null=True, blank=True, default=None)
    logo = models.ImageField(null=True, blank=True, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('main.User', on_delete=models.DO_NOTHING)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class SpaceInvites(models.Model):
    class State:
        PENDING = 'PENDING'
        ACCEPTED = 'ACCEPTED'
        DECLINED = 'DECLINED'

        choices = (
            (PENDING, PENDING),
            (ACCEPTED, ACCEPTED),
            (DECLINED, DECLINED),
        )

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    invitee = models.ForeignKey('main.User', on_delete=models.CASCADE, related_name='invites')
    invited_by = models.ForeignKey('main.User', on_delete=models.CASCADE)
    space = models.ForeignKey('main.Space', on_delete=models.CASCADE)
    date_invited = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=8, choices=State.choices, default=State.PENDING)
    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['invitee', 'space'],
                name='%(app_label)s_%(class)s_unique_invitee_space'),
            models.CheckConstraint(
                check=~models.Q(invitee=models.F('invited_by')),
                name='%(app_label)s_%(class)s_invited_by_is_not_invitee'
            ),
        ]


class SpaceMembership(models.Model):
    class Roles:
        ADMIN = 'ADMIN'
        MEMBER = 'MEMBER'
        VIEWER = 'VIEWER'

        choices = (
            (ADMIN, ADMIN),
            (MEMBER, MEMBER),
            (VIEWER, VIEWER)
        )

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    member = models.ForeignKey('main.User', on_delete=models.CASCADE, related_name="memberships")
    space = models.ForeignKey('main.Space', on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=6, choices=Roles.choices)
    suspended = models.BooleanField(default=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['space', 'member'],
                name="%(app_label)s_%(class)s_unique_space_member"),
        ]

    def __str__(self) -> str:
        return f"{self.member.fullname.replace(' ', '-')}@{self.space.name}"

