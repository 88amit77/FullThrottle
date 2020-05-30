from rest_framework import viewsets
from .serializers import InOutSerializers, MenmbersSerializers, ReportSerializer
from .models import InOut, Members


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MenmbersSerializers


class InOutViewSet(viewsets.ModelViewSet):
    queryset = InOut.objects.all()
    serializer_class = InOutSerializers


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = ReportSerializer