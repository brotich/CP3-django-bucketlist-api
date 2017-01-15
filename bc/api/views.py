from rest_framework import viewsets

from bc.api.models import BucketList
from bc.api.serializers import BucketListSerializer


class BucketListViewSet(viewsets.ModelViewSet):

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer



