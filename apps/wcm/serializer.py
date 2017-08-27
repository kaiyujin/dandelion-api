# coding: utf-8

from rest_framework import serializers

from .models import Period, Status

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('name', 'sort_no', 'ins_at', 'upd_at')
