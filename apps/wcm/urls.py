# coding: utf-8
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'sheets', SheetViewSet)
router.register(r'wills', WillViewSet)
router.register(r'cans', CanViewSet)
router.register(r'musts', MustViewSet)
router.register(r'must_missions', MustMissionViewSet)
