from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def get_published_posts(self):
        return self.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ).order_by('-pub_date')
