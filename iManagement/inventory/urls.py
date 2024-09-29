from django.urls import path
from .views import get_items, manage_item

urlpatterns = [
    path("items/", get_items),
    path("items/<int:item_id>", manage_item)
]