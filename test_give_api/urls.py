from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('stuff_temp', views.stuff_temp_view)









urlpatterns = [
    path('', include(router.urls)),
]
