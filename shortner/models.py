from django.db import models
from django.utils import timezone
from .utils import encode_id
from django.conf import settings


class TinyURL(models.Model):
    original_url = models.URLField()
    short_url_hash = models.TextField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['short_url_hash']),
        ]

    @property
    def short_url(self):
        if self.short_url_hash:
            return "{}/{}".format(settings.BASE_URL, self.short_url_hash)

    def generate_url_hash(self):
        self.short_url_hash = encode_id(self.id)
        self.save()