from django.db import models


class GmtGameId(models.Model):
    game_id = models.CharField(
        max_length=255,
        verbose_name="Bradspelpriset Game ID",
        help_text="get it from bradspelspriser.se",
    )
    game_name = models.CharField(max_length=255)

    def __str__(self):
        return self.game_name
