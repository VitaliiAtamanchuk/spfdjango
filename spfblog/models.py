from django.db import models


class Entry(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name="Publication date",
    )

    class Meta:
        db_table = 'blog_entries'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.headline
