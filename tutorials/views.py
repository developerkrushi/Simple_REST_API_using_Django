from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TutorialSerializer
from .models import Tutorial


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
