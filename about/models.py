from django.db import models

from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

from src.utils import generate_unique_slug

# Create your models here.


class CommandUnit(models.Model):
    job_title = models.CharField(max_length=200, verbose_name="Должность", blank=True)
    fio = models.CharField(max_length=200, verbose_name="ФИО", blank=True)
    email = models.CharField(max_length=50, verbose_name="Email", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True)
    information = models.CharField(
        max_length=1000, verbose_name="Информация", blank=True
    )
    photo = ThumbnailerImageField(
        upload_to="photo/%Y/%m/%d",
        default=None,
        null=True,
        blank=True,
        resize_source=dict(quality=80, size=(1024, 1024)),
        verbose_name="Фото",
    )

    class Meta:
        db_table = "unit"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.job_title


class ValueUnit(models.Model):
    photo = ThumbnailerImageField(
        upload_to="photo/%Y/%m/%d",
        default=None,
        null=True,
        blank=True,
        resize_source=dict(quality=80, size=(1024, 1024)),
        verbose_name="Фото",
    )

    class Meta:
        db_table = "value"
        verbose_name = "Диплом / сертификат"
        verbose_name_plural = "Дипломы / сертификаты от банка"


class JobUnit(models.Model):
    title = models.CharField(max_length=400, verbose_name="Должность", blank=True)
    slug = models.SlugField(
        max_length=410, unique=True, db_index=True, verbose_name="Slug"
    )
    information = models.TextField(
        max_length=3000, verbose_name="Информация", blank=True
    )
    email = models.CharField(max_length=50, verbose_name="Email", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True)

    class Meta:
        db_table = "job"
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = generate_unique_slug(JobUnit, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("about:vacancy", kwargs={"slug": self.slug})
