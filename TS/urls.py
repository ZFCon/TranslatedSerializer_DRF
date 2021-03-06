from django.contrib import admin
from django.urls import path, include

from api.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/test', TestView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
