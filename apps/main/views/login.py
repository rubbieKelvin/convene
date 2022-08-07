from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status

from apps.main.forms.login import LoginForm
from apps.main.sr.users import UserSr

@api_view(['post'])
def main(request: Response) -> Response:
    data = request.data
    form = LoginForm(data=data)

    if not form.is_valid():
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    res = form.validated_data
    return Response({
        "user": UserSr(res["user"]).data,
        "token": res['token'].key
    })