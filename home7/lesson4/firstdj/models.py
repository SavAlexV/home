from django.db import models

# Firstdj:
# title
# description
# price
# auction
# created_at
# updated_at

class Advertisement(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2

    )

    auction = models.BooleanField(
        verbose_name="Торг",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата редактирования",
        auto_now=True
    )

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return "id: {}, title: {}, price: {}".format(self.id, self.title, self.price)