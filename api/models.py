from django.db import models

class Event(models.Model):

    STATUS_CHOICES = [
        ('upcoming', 'À venir'),
        ('ongoing', 'En cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ]
    
    name = models.CharField(max_length=100)
    date = models.DateField()
    hour = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming') 
    
    def __str__(self):
        return self.name


class Participant(models.Model):
    GENDER_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    events = models.ManyToManyField(Event, through='Registration')

    def __str__(self):
        return self.name


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participant.name} registered for {self.event.name}"

    class Meta:
        unique_together = ('event', 'participant')