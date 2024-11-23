from django.urls import path, include
from rest_framework import routers

from api.views import FoodCategoryViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('foods', FoodCategoryViewSet, basename='foods')

urlpatterns = [
    path('v1/', include(router.urls)),
]
