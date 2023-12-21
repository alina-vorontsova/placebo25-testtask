from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    ManyToManyField,
    SET_NULL,
)


class Divisions(Model):
    name = CharField(max_length=50, unique=True, verbose_name="Название подразделения")
    main_division = ForeignKey(
        "self",
        related_name="subdivisions",
        on_delete=SET_NULL,
        null=True,
        verbose_name="Главное подразделение",
    )

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.name


class Positions(Model):
    name = CharField(max_length=40, verbose_name="Название должности")
    divisions = ManyToManyField(
        Divisions,
        related_name="positions",
        verbose_name="Подразделение",
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class Staff(Model):
    name = CharField(max_length=100, verbose_name="Имя сотрудника")
    positions = ManyToManyField(
        Positions, related_name="staff", verbose_name="Должности"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name


class Permissions(Model):
    name = CharField(max_length=50, verbose_name="Разрешение")
    positions = ManyToManyField(
        Positions,
        related_name="permissions",
        verbose_name="Должность",
    )

    class Meta:
        verbose_name = "Разрешение"
        verbose_name_plural = "Разрешения"

    def __str__(self):
        return self.name
