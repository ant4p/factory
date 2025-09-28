from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

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
