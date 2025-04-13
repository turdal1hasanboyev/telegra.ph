from django.db import models

from django.urls import reverse
from django.utils.text import slugify

from uuid import uuid4
from datetime import datetime


class Post(models.Model):
    """
    Model for blog posts.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    edit_token = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            date_str = datetime.today().strftime('%d-%m-%Y-%H-%M-%S')
            unique_id = uuid4().hex[:8]
            self.slug = f"{base_slug}-{date_str}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
