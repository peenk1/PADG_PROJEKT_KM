class Restauracja:
    def __init__(self, nazwa, lat, lon):
        self.nazwa = nazwa
        self.lat = lat
        self.lon = lon

class Pracownik:
    def __init__(self, imie, nazwisko, restauracja, lat, lon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.restauracja = restauracja
        self.lat = lat
        self.lon = lon

class Klient:
    def __init__(self, imie, nazwisko, restauracja, lat, lon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.restauracja = restauracja
        self.lat = lat
        self.lon = lon

lista_restauracji = []
lista_pracownikow = []
lista_klientow = []