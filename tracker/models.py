from django.db import models
from django.contrib.postgres.fields import JSONField


class GmtGameId(models.Model):
    game_id = models.CharField(
        max_length=255,
        verbose_name="Bradspelpriset Game ID",
        help_text="get it from bradspelspriser.se",
    )
    game_name = models.CharField(max_length=255)

    def __str__(self):
        return self.game_name


class GmtGameLog(models.Model):
    game_id = models.ForeignKey(GmtGameId, on_delete=models.CASCADE)
    html = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    stores = JSONField()

    def __str__(self):
        return f"{self.game_id.game_name} - {self.date_added}"
