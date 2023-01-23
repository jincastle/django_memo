from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
import jwt, datetime

from .serializers import SignUpSerializer, LoginSerializer


# Create your views here.
class SignUpAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        ser = SignUpSerializer(data=request.data)

        try:
            ser.is_valid(raise_exception=True)
            user = ser.save()
            return Response(user.generate_token(), status=200)

        except Exception:
            return Response({'succsess': False}, status=404)


class LoginApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        ser = LoginSerializer(data=request.data)
        try:
            ser.is_valid(raise_exception=True)
            print(ser.validated_data.get('email'))
            user = User.objects.get(email=ser.validated_data.get('email'))
            token_list = OutstandingToken.objects.filter(user=user)  # 기존 토큰 블렉리스트 처리

            for token in token_list:
                try:
                    RefreshToken(token.token).blacklist()
                except TokenError:
                    pass
            return Response(user.generate_token(), status=200)

        except Exception:
            return Response({'succsess': False}, status=404)