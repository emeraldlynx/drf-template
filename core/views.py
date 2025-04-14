from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view
from rest_framework import generics

from core.serializers import UserSerializer


@extend_schema(tags=["Profile"])
class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.select_related('settings')

    def get_object(self):
        return self.request.user
