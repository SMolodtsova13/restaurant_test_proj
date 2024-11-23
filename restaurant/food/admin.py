from django.contrib import admin

from food.models import Food, FoodCategory


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'order_id')
    search_fields = ('name_ru', 'order_id')
    list_filter = ('order_id',)
    empty_value_display = 'Поле не заполнено'


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'code', 'name_ru','is_publish')
    empty_value_display = 'Поле не заполнено'


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)