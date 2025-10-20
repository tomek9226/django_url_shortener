from django.db import models
import random
import string


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=6))
        super().save(*args, **kwargs)
