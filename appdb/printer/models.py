from django.db import models


class Printer(models.Model):
    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"

    serial = models.CharField(
        max_length=32, db_index=True,
        verbose_name="Серийный номер",
        default=''
    )
    name = models.CharField(
        max_length=64, verbose_name="Наименование", default='Printer'
    )
    page_count_total = models.PositiveIntegerField(
        default=0, verbose_name="Счетчик отпечатков общий"
    )
    page_count_color = models.PositiveIntegerField(
        default=0, verbose_name="Счетчик цветных отпечатков"
    )
    model = models.ForeignKey(
        "Model",
        on_delete=models.CASCADE,
        verbose_name="Модель принтера",
    )

    def __str__(self):
        return self.name


class PrinterCount(models.Model):
    class Meta:
        verbose_name = "Счетчики принтера"
        verbose_name_plural = "Счетчики принтеров"

    date_getting = models.DateField(verbose_name="Дата показателей")

    page_count_total = models.PositiveIntegerField(
        default=0, verbose_name="Счетчик отпечатков общий"
    )

    page_count_color = models.PositiveIntegerField(
        default=0, verbose_name="Счетчик цветных отпечатков"
    )

    printer = models.ForeignKey(
        "Printer",
        on_delete=models.CASCADE,
        verbose_name="Принтер",
    )


class Part(models.Model):
    class Meta:
        verbose_name = "Запчасть принтера"
        verbose_name_plural = "Запчасти принтеров"

    name = models.CharField(
        max_length=64, verbose_name="Наименование"
    )

    model = models.ForeignKey(
        "Model",
        on_delete=models.CASCADE,
        verbose_name="Модель принтера",
    )

    resource = models.PositiveIntegerField(
        default=0,
        verbose_name="Ресурс ",
        help_text='На какое количество страниц рассчитан'
    )

    def __str__(self):
        return self.name


class Model(models.Model):
    class Meta:
        verbose_name = "Модель принтера"
        verbose_name_plural = "Модели принтеров"

    name = models.CharField(
        max_length=64, verbose_name="Наименование"
    )

    class Meta:
        verbose_name = "Модель принтера"
        verbose_name_plural = "Модели принтеров"

    def __str__(self):
        return self.name
