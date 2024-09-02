from django.contrib import admin
from django.urls import path
from myapp.views import add_item, index, getItems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_item, name='add_item'),
    path('', index, name='index'),
    path('get_items/', getItems, name='get_items'),
]
