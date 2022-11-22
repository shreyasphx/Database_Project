from rest_framework import routers
from django.urls import path, include
from connection.views import ConnectionViewSet
from query.views import QueryViewSet

router = routers.DefaultRouter()
router.register(r'connections', ConnectionViewSet)
router.register(r'queries',QueryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace = 'rest_framework'))
]