from rest_framework import routers
from django.urls import path, include

from .views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
