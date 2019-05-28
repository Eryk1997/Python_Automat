from PrzechowywaczMonet import *
from Menu import *
import tkinter.messagebox

class Automat(PrzechowywaczMonet):
    def __init__(self):
        super().__init__()
        self._okno = Tk()
        self._okno.title("Automat")
        self._doZaplaty = Decimal('0')
        self._reszta = 0
        self._listaIloscBiletow = [0, 0, 0, 0, 0, 0]
        self._menu = Menu()
        self._menu.wyswietlBilety()
        self._reverse = False
        self.doZaplaty()
        self._menu.wyswietlMonety()
        self.monety()
        self.listaPrzechowujacaMonetyTymczasowo = []


    def addMoneta(self, wartosc: Moneta):
        super().addMoneta(wartosc)

    def wrzucMonete(self, wartosc: Moneta):
        super().wrzucMonete(wartosc)
        if self.getDoZaplaty() - self.getSumaWrzuconychMonet() <= Decimal('0'):
            self.reszta()
        self._menu._labelDoZaplaty["text"] = "Do zapłaty= " + str(
            self.getDoZaplaty() - self.getSumaWrzuconychMonet()) + "zł"

    def getSumaWrzuconychMonet(self):
        return super().getSumaWrzuconychMonet()

    def getSumaMonet(self):
        return super().getSumaMonet()

    def getDoZaplaty(self):
        return round(self._doZaplaty, 2)

    def getReszta(self):
        return round(self._reszta, 2)

    def tworzenieListyMonetReszty(self, lista):
        nowaLista = []
        for i in lista:
            nowaLista.append(str(i) + "zł ")
        return nowaLista

    def komunikatBrakReszty(self):
        text = "Nie ma z czego wydać, tylko wyliczona kwota! \n"
        for i in self.wrzuconeMonety:
            text += str(i.getWartosc()) + "zł "
        return text

    def tworzenieListyAnuluj(self):
        text = "Odbierz monety: \n"
        for i in self.wrzuconeMonety:
            text += str(i.getWartosc()) + "zł "
        return text


    def tworzenieListyZIlosciaBiletow(self):
        listaText = [" biletów 20min normalnych", " biletów 20min ulgowych", " biletów 40min normalnych", " biletów 40min ulgowych", " biletów 60min normalnych", " biletów 60min ulgowych", ]
        nowaLista = []
        for i in range(len(self._listaIloscBiletow)):
            if self._listaIloscBiletow[i] > 0:
                nowaLista.append("Kupiłeś: " + str(self._listaIloscBiletow[i]/self._listaIloscBiletow[i]) + listaText[i])
        return nowaLista

    def sumaDoZaplaty(self, x):
        if x == 0:
            self._listaIloscBiletow[0] = 2.8 * int(self._menu._iloscBiletow[0].get())
        if x == 1:
            self._listaIloscBiletow[1] = 1.4 * int(self._menu._iloscBiletow[1].get())
        if x == 2:
            self._listaIloscBiletow[2] = 5.6 * int(self._menu._iloscBiletow[2].get())
        if x == 3:
            self._listaIloscBiletow[3] = 2.8 * int(self._menu._iloscBiletow[3].get())
        if x == 4:
            self._listaIloscBiletow[4] = 8.4 * int(self._menu._iloscBiletow[4].get())
        if x == 5:
            self._listaIloscBiletow[5] = 4.2 * int(self._menu._iloscBiletow[5].get())

        self._doZaplaty = Decimal(self._listaIloscBiletow[0] + self._listaIloscBiletow[1] + self._listaIloscBiletow[2] +
                                  self._listaIloscBiletow[3] + self._listaIloscBiletow[4] + self._listaIloscBiletow[5])

        self._menu._labelDoZaplaty["text"] = "Do zapłaty= " + str(
            self.getDoZaplaty() - self.getSumaWrzuconychMonet()) + "zł"
        self._menu._labelDoZaplaty.grid(row=5, column=2)

    def doZaplaty(self):
        self._menu._iloscBiletow[0]["command"] = lambda: self.sumaDoZaplaty(0)
        self._menu._iloscBiletow[1]["command"] = lambda: self.sumaDoZaplaty(1)
        self._menu._iloscBiletow[2]["command"] = lambda: self.sumaDoZaplaty(2)
        self._menu._iloscBiletow[3]["command"] = lambda: self.sumaDoZaplaty(3)
        self._menu._iloscBiletow[4]["command"] = lambda: self.sumaDoZaplaty(4)
        self._menu._iloscBiletow[5]["command"] = lambda: self.sumaDoZaplaty(5)

    def monety(self):
        self._menu._monety[0]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.01')))
        self._menu._monety[1]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.02')))
        self._menu._monety[2]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.05')))
        self._menu._monety[3]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.1')))
        self._menu._monety[4]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.2')))
        self._menu._monety[5]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('0.5')))
        self._menu._monety[6]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('1')))
        self._menu._monety[7]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('2')))
        self._menu._monety[8]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('5')))
        self._menu._monety[9]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('10')))
        self._menu._monety[10]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('20')))
        self._menu._monety[11]["command"] = lambda: self.wrzucMonete(Moneta(Decimal('50')))

        Button(text="anuluj",command=self.anuluj).grid(row=8,column=0)

    def anuluj(self):
        tkinter.messagebox.showinfo("Komunikat", str(self.tworzenieListyAnuluj()))
        self.zerowanieSpinBox()

    def zerowanieSpinBox(self):
        for i in range(6):
            self._menu._iloscBiletow[i].delete(0)
            self._menu._iloscBiletow[i].insert(i, 0)
            self._listaIloscBiletow[i] = 0
        self.wrzuconeMonety.clear()
        self._doZaplaty = 0
        self._menu._labelDoZaplaty["text"] = "Do zapłaty= 0zł"
        self.listaPrzechowujacaMonetyTymczasowo.clear()

    def reszta(self):
        self._reszta = self.getSumaWrzuconychMonet() - self.getDoZaplaty()
        if self._reverse == False:
            self._bank.reverse()
            self._reverse = True
        resztaDoWydania = 0

        for i in range(len(self._bank)):
            if self.getReszta() == Decimal('0'):
                for i in self.wrzuconeMonety:
                    self._bank.append(i)
                if resztaDoWydania > 0:
                    tkinter.messagebox.showinfo("Komunikat", "Odbierz reszte: " + str(resztaDoWydania) + "zł \n" + str(
                        self.tworzenieListyMonetReszty(self.listaPrzechowujacaMonetyTymczasowo)) + "\n" + str(
                        self.tworzenieListyZIlosciaBiletow()))

                elif resztaDoWydania == 0:
                    tkinter.messagebox.showinfo("Komunikat", str(self.tworzenieListyZIlosciaBiletow()))
                self.zerowanieSpinBox()

                break
            elif round(self.getReszta() / self._bank[i].getWartosc(), 2) >= 1 and self.getReszta() > 0:
                self._reszta -= self._bank[i].getWartosc()
                self.listaPrzechowujacaMonetyTymczasowo.append(self._bank[i].getWartosc())
                resztaDoWydania += self._bank[i].getWartosc()
                del self._bank[i]
        if self.getReszta() > 0:
            tkinter.messagebox.showinfo("Konunikat",self.komunikatBrakReszty())
            for i in self.listaPrzechowujacaMonetyTymczasowo:
                self.addMoneta(i)
            self.wrzuconeMonety.clear()
            self._doZaplaty = 0
            self._menu._labelDoZaplaty["text"] = "Do zapłaty= 0zł"





