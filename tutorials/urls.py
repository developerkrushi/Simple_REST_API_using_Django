from django.urls import include, path
from rest_framework import routers
from .views import TutorialViewSet

router = routers.DefaultRouter()
router.register(r'tutorial', TutorialViewSet)

urlpatterns = [
   path('', include(router.urls)),
]