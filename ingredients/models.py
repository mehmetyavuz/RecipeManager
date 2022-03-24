from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(null=False, max_length=200)
    article_number = models.IntegerField(null=False)
    unit = models.ForeignKey(Unit, null=False, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(null=False)
    cost = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def description(self):
        return '{} {} €{}'.format(self.amount, self.unit.name, self.cost)

