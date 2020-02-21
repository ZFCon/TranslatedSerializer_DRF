from rest_framework import generics

from . import models
from . import serializers


class TestView(generics.ListAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
