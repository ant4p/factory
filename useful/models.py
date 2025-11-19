from django.db import models
from django.urls import reverse

from easy_thumbnails.fields import ThumbnailerImageField
from src.utils import generate_unique_slug


class Article(models.Model):
    CHOICE = (
        ("Статья", "Статья"),
        ("Ссылка", "Ссылка"),
    )
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    choice = models.CharField(
        max_length=100,
        choices=CHOICE,
        default="Статья",
        null=True,
        blank=True,
        verbose_name="Вид",
    )
    slug = models.SlugField(
        max_length=310, unique=True, db_index=True, verbose_name="Slug"
    )
    content = models.TextField(blank=True, verbose_name="Текст статьи")

    class Meta:
        db_table = "article"
        verbose_name = "Статья / Ссылка"
        verbose_name_plural = "Статьи / Ссылки"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = generate_unique_slug(Article, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("useful:useful_article", kwargs={"slug": self.slug})


class Document(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=310, unique=True, db_index=True, verbose_name="Slug"
    )
    image = ThumbnailerImageField(
        upload_to="photo/%Y/%m/%d",
        default=None,
        null=True,
        blank=True,
        resize_source=dict(quality=80, size=(500, 500)),
        verbose_name="Фото",
    )
    content = models.TextField(blank=True, verbose_name="Текст")

    class Meta:
        db_table = "document"
        verbose_name = "Нормативный документ"
        verbose_name_plural = "Нормативныe документы"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = generate_unique_slug(Document, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("useful:useful_document", kwargs={"slug": self.slug})
