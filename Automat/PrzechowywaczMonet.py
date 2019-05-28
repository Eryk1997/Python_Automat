from Moneta import *


class PrzechowywaczMonet:

    def __init__(self):
        self._bank = []
        self.wrzuconeMonety = []
        monety = [Moneta(Decimal('0.01')), Moneta(Decimal('0.02')), Moneta(Decimal('0.05')), Moneta(Decimal('0.1')),
                  Moneta(Decimal('0.2')), Moneta(Decimal('0.5')), Moneta(Decimal('1')), Moneta(Decimal('2')),
                  Moneta(Decimal('5')), Moneta(Decimal('10')), Moneta(Decimal('20')), Moneta(Decimal('50'))]

        for i in range(12):
            for j in range(100):
                self._bank.append(monety[i])

    def addMoneta(self, wartosc: Moneta):
        if isinstance(wartosc, Moneta):
            self._bank.append(wartosc)

    def getSumaMonet(self):
        return sum(Moneta.getWartosc() for Moneta in self._bank)

    def wrzucMonete(self, wartosc: Moneta):
        if isinstance(wartosc, Moneta):
            self.wrzuconeMonety.append(wartosc)

    def getSumaWrzuconychMonet(self):
        return sum(Moneta.getWartosc() for Moneta in self.wrzuconeMonety)