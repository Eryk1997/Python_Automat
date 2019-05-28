from decimal import *


class Moneta:
    def __init__(self, wartosc):
        if wartosc in (
                Decimal('0.01'), Decimal('0.02'), Decimal('0.05'), Decimal('0.1'), Decimal('0.2'), Decimal('0.5'),
                Decimal('1'),
                Decimal('2'), Decimal('5'), Decimal('10'), Decimal('20'), Decimal('50')):
            self._wartosc = wartosc

    def getWartosc(self):
        return self._wartosc