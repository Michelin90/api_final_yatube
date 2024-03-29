from rest_framework import viewsets
from rest_framework.generics import mixins


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass
