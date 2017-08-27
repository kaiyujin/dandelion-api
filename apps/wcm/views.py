# coding: utf-8
import django_filters
from rest_framework import viewsets, filters
from django.shortcuts import render
from django.http import HttpResponse
from .models import Status, Period
from .serializer import PeriodSerializer

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
