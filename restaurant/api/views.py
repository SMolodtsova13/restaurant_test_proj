from rest_framework import viewsets

from api.serializers import FoodListSerializer
from food.models import FoodCategory


class FoodCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для получения списка блюд."""
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer

    def get_queryset(self):
        categories = super().get_queryset()        
        return categories.filter(food__is_publish=True)
