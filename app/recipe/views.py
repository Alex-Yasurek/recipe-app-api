from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """return objects for the current authenticated user only"""
        # overwrite return by making sure only tags created by user making request
        # are return. request object will have user object since authentication
        # is required because of auth_classes and permission_classes
        return self.queryset.filter(user=self.request.user).order_by('-name')
