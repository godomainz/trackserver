from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Track
from track import serializers


class BaseTrackViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        assigned_only = bool(int(self.request.query_params.get('assigned_only', 0)))
        queryset = self.queryset

        if assigned_only:
            queryset = queryset.filter(track__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TrackViewSet(BaseTrackViewSet):
    """Manage tags in the database"""
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
