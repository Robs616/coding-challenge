from .models import Buzzword
from rest_framework import viewsets
from .serializers import BuzzwordSerializer

#rest framework for buzzwords /buzzwords/list/ 
class BuzzwordViewSet(viewsets.ModelViewSet):
    queryset = Buzzword.objects.all().order_by('name')
    serializer_class = BuzzwordSerializer