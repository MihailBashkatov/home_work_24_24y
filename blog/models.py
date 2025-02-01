from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Post titles", help_text="Insert title of the post"
    )
    content = models.TextField(
        verbose_name="Full content", help_text="Insert content of the post"
    )
    picture = models.ImageField(
        upload_to="blog/images/",
        verbose_name="Post images",
        blank=True,
        null=True,
        help_text="Upload picture",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creating a post",
        help_text="Insert date and time when post is created",
    )
    is_published = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(
        default=0, verbose_name="Amount of views"
    )


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title",]
