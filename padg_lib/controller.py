from padg_lib import map_service
from padg_lib.model import *

# Słowniki do przechowywania markerów
markery_restauracji = {}
markery_pracownikow = {}
markery_klientow = {}


class RestauracjaController:
    def __init__(self, map_widget, listbox_restauracji, listbox_pracownikow, listbox_klientow):
        self.map_widget = map_widget
        self.listbox_restauracji = listbox_restauracji
        self.listbox_pracownikow = listbox_pracownikow
        self.listbox_klientow = listbox_klientow

    def dodaj(self, nazwa, lat, lon):
        r = Restauracja(nazwa, lat, lon)
        lista_restauracji.append(r)
        self.listbox_restauracji.insert("end", r.nazwa)
        marker = map_service.add_restaurant_marker(self.map_widget, float(r.lat), float(r.lon), r.nazwa)
        markery_restauracji[r] = marker
        return r

    def edytuj(self, idx, nazwa, lat, lon):
        r = lista_restauracji[idx]

        # Usuń stary marker
        if r in markery_restauracji:
            markery_restauracji[r].delete()

        # Zapisz starą nazwę
        stara_nazwa = r.nazwa

        # Aktualizuj dane
        r.nazwa = nazwa
        r.lat = lat
        r.lon = lon

        # Aktualizuj nazwę restauracji u wszystkich pracowników
        for p in lista_pracownikow:
            if p.restauracja == stara_nazwa:
                p.restauracja = r.nazwa

        # Aktualizuj nazwę restauracji u wszystkich klientów
        for k in lista_klientow:
            if k.restauracja == stara_nazwa:
                k.restauracja = r.nazwa

        # Odśwież listboxy
        self._odswiez_listboxy()

        # Dodaj nowy marker
        marker = map_service.add_restaurant_marker(self.map_widget, float(r.lat), float(r.lon), r.nazwa)
        markery_restauracji[r] = marker

    def usun(self, idx):
        r = lista_restauracji[idx]

        # Usuń marker z mapy
        if r in markery_restauracji:
            markery_restauracji[r].delete()
            del markery_restauracji[r]

        # Odepnij restaurację od pracowników i klientów
        for p in lista_pracownikow:
            if p.restauracja == r.nazwa:
                p.restauracja = ""

        for k in lista_klientow:
            if k.restauracja == r.nazwa:
                k.restauracja = ""

        # Odśwież listboxy
        self._odswiez_listboxy()

        # Usuń z listy
        lista_restauracji.pop(idx)
        self.listbox_restauracji.delete(idx)

    def pokaz_na_mapie(self, idx):
        r = lista_restauracji[idx]
        self.map_widget.set_position(float(r.lat), float(r.lon))
        self.map_widget.set_zoom(15)

    def _odswiez_listboxy(self):
        self.listbox_pracownikow.delete(0, "end")
        for p in lista_pracownikow:
            self.listbox_pracownikow.insert("end", f"{p.imie} {p.nazwisko} {p.restauracja}")

        self.listbox_klientow.delete(0, "end")
        for k in lista_klientow:
            self.listbox_klientow.insert("end", f"{k.imie} {k.nazwisko} {k.restauracja}")


class PracownikController:
    def __init__(self, map_widget, listbox_pracownikow):
        self.map_widget = map_widget
        self.listbox_pracownikow = listbox_pracownikow

    def dodaj(self, imie, nazwisko, restauracja, lat, lon):
        p = Pracownik(imie, nazwisko, restauracja, lat, lon)
        lista_pracownikow.append(p)
        self.listbox_pracownikow.insert("end", f"{p.imie} {p.nazwisko} {p.restauracja}")
        marker = map_service.add_employee_marker(self.map_widget, float(p.lat), float(p.lon), f"{p.imie} {p.nazwisko}")
        markery_pracownikow[p] = marker
        return p

    def edytuj(self, idx, imie, nazwisko, restauracja, lat, lon):
        p = lista_pracownikow[idx]

        # Usuń stary marker
        if p in markery_pracownikow:
            markery_pracownikow[p].delete()

        # Aktualizuj dane
        p.imie = imie
        p.nazwisko = nazwisko
        p.restauracja = restauracja
        p.lat = lat
        p.lon = lon

        # Aktualizuj listbox
        self.listbox_pracownikow.delete(idx)
        self.listbox_pracownikow.insert(idx, f"{p.imie} {p.nazwisko} {p.restauracja}")
        self.listbox_pracownikow.selection_set(idx)

        # Dodaj nowy marker
        marker = map_service.add_employee_marker(self.map_widget, float(p.lat), float(p.lon), f"{p.imie} {p.nazwisko}")
        markery_pracownikow[p] = marker

    def usun(self, idx):
        p = lista_pracownikow[idx]

        # Usuń marker z mapy
        if p in markery_pracownikow:
            markery_pracownikow[p].delete()
            del markery_pracownikow[p]

        # Usuń z listy
        lista_pracownikow.pop(idx)
        self.listbox_pracownikow.delete(idx)

    def pokaz_na_mapie(self, idx):
        p = lista_pracownikow[idx]
        self.map_widget.set_position(float(p.lat), float(p.lon))
        self.map_widget.set_zoom(15)


class KlientController:
    def __init__(self, map_widget, listbox_klientow):
        self.map_widget = map_widget
        self.listbox_klientow = listbox_klientow

    def dodaj(self, imie, nazwisko, restauracja, lat, lon):
        k = Klient(imie, nazwisko, restauracja, lat, lon)
        lista_klientow.append(k)
        self.listbox_klientow.insert("end", f"{k.imie} {k.nazwisko} {k.restauracja}")
        marker = map_service.add_client_marker(self.map_widget, float(k.lat), float(k.lon), f"{k.imie} {k.nazwisko}")
        markery_klientow[k] = marker
        return k

    def edytuj(self, idx, imie, nazwisko, restauracja, lat, lon):
        k = lista_klientow[idx]

        # Usuń stary marker
        if k in markery_klientow:
            markery_klientow[k].delete()

        # Aktualizuj dane
        k.imie = imie
        k.nazwisko = nazwisko
        k.restauracja = restauracja
        k.lat = lat
        k.lon = lon

        # Aktualizuj listbox
        self.listbox_klientow.delete(idx)
        self.listbox_klientow.insert(idx, f"{k.imie} {k.nazwisko} {k.restauracja}")
        self.listbox_klientow.selection_set(idx)

        # Dodaj nowy marker
        marker = map_service.add_client_marker(self.map_widget, float(k.lat), float(k.lon), f"{k.imie} {k.nazwisko}")
        markery_klientow[k] = marker

    def usun(self, idx):
        k = lista_klientow[idx]

        # Usuń marker z mapy
        if k in markery_klientow:
            markery_klientow[k].delete()
            del markery_klientow[k]

        # Usuń z listy
        lista_klientow.pop(idx)
        self.listbox_klientow.delete(idx)

    def pokaz_na_mapie(self, idx):
        k = lista_klientow[idx]
        self.map_widget.set_position(float(k.lat), float(k.lon))
        self.map_widget.set_zoom(15)