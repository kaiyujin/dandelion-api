# coding: utf-8

from rest_framework import serializers

from .models import *


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('name', 'sort_no', 'ins_at', 'upd_at')


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = ('user', 'period', 'status')


class WillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Will
        fields = ('sheet', 'realize_member', 'realize_manager',
                  'career_image_member', 'career_image_manager')


class CanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Can
        fields = ('sheet', 'strength_member', 'strength_manager',
                  'weekness_member', 'weekness_manager', 'action', 'evaluation')


class MustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Must
        fields = ('sheet', 'thema', 'content', 'evaluation', 'score_member')


class MustMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MustMission
        fields = ('must', 'goal', 'process', 'to_report', 'score_member',
                  'criteria', 'weight', 'result', 'score_member', 'score_manager')