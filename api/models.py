from django.db import models


class Gem(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Client(models.Model):
    username = models.CharField(max_length=128)
    money_spent = models.IntegerField()
    gems = models.ManyToManyField(Gem)

    def __str__(self):
        return self.username


class Deal(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Gem, on_delete=models.CASCADE)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.customer} bought {self.item}'
