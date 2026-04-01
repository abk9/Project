from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event, Participant, Registration
from .serializers import EventSerializer, ParticipantSerializer, RegistrationSerializer
from .permissions import IsEditorOrReadOnly # <-- Import de ta nouvelle permission

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Application de la permission ici :
    permission_classes = [IsAuthenticated, IsEditorOrReadOnly]

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    # Application de la permission ici :
    permission_classes = [IsAuthenticated, IsEditorOrReadOnly]

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    # Application de la permission ici :
    permission_classes = [IsAuthenticated, IsEditorOrReadOnly]