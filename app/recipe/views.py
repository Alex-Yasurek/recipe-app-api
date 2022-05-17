from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe import serializers


class BaseRecipeAttrViewset(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):

    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """"Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewset):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    # def get_queryset(self):
    #     """return objects for the current authenticated user only"""
    #     # overwrite return by making sure only tags created by user making request
    #     # are return. request object will have user object since authentication
    #     # is required because of auth_classes and permission_classes
    #     return self.queryset.filter(user=self.request.user).order_by('-name')

    # def perform_create(self, serializer):
    #     """Create a new tag"""
    #     serializer.save(user=self.request.user)


class IngredientViewSet(BaseRecipeAttrViewset):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    # def get_queryset(self):
    #     """return objects for current authenticated user"""
    #     return self.queryset.filter(user=self.request.user).order_by('-name')

    # def perform_create(self, serializer):
    #     """Create new ingredient"""
    #     serializer.save(user=self.request.user)
