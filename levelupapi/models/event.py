from django.db import models
from django.db.models.deletion import CASCADE

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete = CASCADE)
    organizer = models.ForeignKey("Gamer", on_delete = CASCADE)
    description = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    participants = models.ManyToManyField(
        "Gamer",
        related_name = "participant_events",
        related_query_name ="participant_event"
    )
