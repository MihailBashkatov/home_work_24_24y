from django.db import models


class Author(models.Model):
    author_name = models.CharField(
        max_length=150,
        verbose_name="Author name",
        help_text="insert name of the author",
    )

    def __str__(self):
        return f"{self.author_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["author_name"]


class Blog(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Post titles", help_text="Insert title of the post"
    )
    content = models.TextField(
        verbose_name="Full content", help_text="Insert content of the post"
    )
    picture = models.ImageField(
        upload_to="images/",
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
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name="authors",
        verbose_name="Author of the post",
        help_text="Insert author of the post",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "author"]
