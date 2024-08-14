from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from admin_panel.serializers.user.auth import CustomAuthTokenSerializer


class CustomAuthTokenView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        token, created = Token.objects.get_or_create(user=user)
        organization = None
        if user and user.employee:
            organization = user.employee.organization_id
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'organization': organization,
            'email': user.email
        })
