# coding: utf-8
import django_filters
from rest_framework import viewsets, filters
from .models import *
from .serializer import *


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class WillViewSet(viewsets.ModelViewSet):
    queryset = Will.objects.all()
    serializer_class = WillSerializer


class CanViewSet(viewsets.ModelViewSet):
    queryset = Can.objects.all()
    serializer_class = CanSerializer


class MustViewSet(viewsets.ModelViewSet):
    queryset = Must.objects.all()
    serializer_class = MustSerializer


class MustMissionViewSet(viewsets.ModelViewSet):
    queryset = MustMission.objects.all()
    serializer_class = MustMissionSerializer
