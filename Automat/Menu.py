from tkinter import *

class Menu(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self.bilety = []
        self._iloscBiletow = []
        for i in range(6):
            self._iloscBiletow.append(Spinbox(width=3, from_=0, to=100, fg="blue"))
            self.bilety.append(Label())


        self._labelDoZaplaty = Label()
        self._monety = []
        self.labelSumaWrzuconychMonet = Label()
        self.labelSumaDoZaplaty = Label()
        self.buttonZaplac = Button()
        self.buttonDodajBilet = Button()
        self.nazwy = ['0.01', '0.02', '0.05', '0.10', '0.20', '0.50', '1.00', '2.00', '5.00', '10.00', '20.00', '50.00']
        for i in self.nazwy:
            self._monety.append(Button(text=str(i) + "zł"))

    def wyswietlMonety(self):
        for i in range(6,18):
            if i < 12:
                self._monety[i-6].grid(row=6, column=i-6)
            else:
                self._monety[i-6].grid(row=7, column=i - 12)



    def wyswietlBilety(self):
        self.bilety[0]["text"] = "Normalny 20min"
        self.bilety[1]["text"] = "Ulgowy 20min"
        self.bilety[2]["text"] = "Normalny 40min"
        self.bilety[3]["text"] = "Ulgowy 40min"
        self.bilety[4]["text"] = "Normalny 60min"
        self.bilety[5]["text"] = "Ulgowy 60min"
        self.zaplac = Button(text="Zapłać")

        for i in range(6):
            if i % 2 == 0:
                self.bilety[i].grid(row=i, column=0)
                self._iloscBiletow[i].grid(row=i, column=1)
            else:
                self.bilety[i].grid(row=i - 1, column=3)
                self._iloscBiletow[i].grid(row=i - 1, column=2)











