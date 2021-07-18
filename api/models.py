from django.db import models


class Deal(models.Model):

    gems = (
        ('Цаворит', 'Цаворит'),
        ('Сапфир', 'Сапфир'),
        ('Рубин', 'Рубин'),
        ('Яшма', 'Яшма'),
        ('Берилл', 'Берилл'),
        ('Опал', 'Опал'),
        ('Изумруд', 'Изумруд'),
        ('Спессартин', 'Спессартин'),
        ('Сердолик', 'Сердолик'),
        ('Кварц', 'Кварц'),
        ('Аквамарин', 'Аквамарин'),
        ('Аметрин', 'Аметрин'),
        ('Циркон', 'Циркон'),
        ('Топаз', 'Топаз'),
        ('Танзанит', 'Танзанит'),
        ('Петерсит', 'Петерсит'),
        ('Бирюза', 'Бирюза'),
        ('Хризоберилл', 'Хризоберилл'),
        ('Хризолит', 'Хризолит'),
        ('Халцедон', 'Халцедон'),
        ('Марганит', 'Марганит'),
        ('Петерсит', 'Петерсит'),
        ('Аметист', 'Аметист'),
        ('Лунный камень', 'Лунный камень'),
        ('Жемчуг', 'Жемчуг'),
    )

    customer = models.CharField(max_length=128)
    item = models.CharField(choices=gems, max_length=128)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.customer} bought {self.item}'


class Client(models.Model):
    username = models.CharField(max_length=128)
    money_spent = models.IntegerField()
    # gems = models.Field

    def __str__(self):
        return self.username
