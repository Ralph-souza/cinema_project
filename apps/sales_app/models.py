from django.db import models

from apps.admin_app.models import Movies, Rooms, Teather


class Tickets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    teather = models.ForeignKey(Teather, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.movie.title
