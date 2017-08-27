from rest_framework import routers
from .views import PeriodViewSet

router = routers.DefaultRouter()
router.register(r'periods', PeriodViewSet)
