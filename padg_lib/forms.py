from tkinter import *
from tkinter import ttk
from padg_lib.model import lista_restauracji


class RestauracjaForm:
    def __init__(self, parent, controller, edit_mode=False, idx=None, restauracja=None):
        self.okno = Toplevel(parent)
        self.okno.title("Edytuj restaurację" if edit_mode else "Dodaj restaurację")
        self.controller = controller
        self.edit_mode = edit_mode
        self.idx = idx

        Label(self.okno, text="Nazwa:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_nazwa = Entry(self.okno, width=30)
        self.entry_nazwa.grid(row=0, column=1, padx=5, pady=5)

        Label(self.okno, text="Lat:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_lat = Entry(self.okno, width=30)
        self.entry_lat.grid(row=1, column=1, padx=5, pady=5)

        Label(self.okno, text="Lon:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_lon = Entry(self.okno, width=30)
        self.entry_lon.grid(row=2, column=1, padx=5, pady=5)

        if edit_mode and restauracja:
            self.entry_nazwa.insert(0, restauracja.nazwa)
            self.entry_lat.insert(0, restauracja.lat)
            self.entry_lon.insert(0, restauracja.lon)

        btn_text = "Zapisz" if edit_mode else "Dodaj"
        Button(self.okno, text=btn_text, command=self.zapisz).grid(
            row=3, column=0, columnspan=2, pady=10
        )

    def zapisz(self):
        nazwa = self.entry_nazwa.get()
        lat = self.entry_lat.get()
        lon = self.entry_lon.get()

        if self.edit_mode:
            self.controller.edytuj(self.idx, nazwa, lat, lon)
        else:
            self.controller.dodaj(nazwa, lat, lon)

        self.okno.destroy()


class PracownikForm:
    def __init__(self, parent, controller, edit_mode=False, idx=None, pracownik=None):
        self.okno = Toplevel(parent)
        self.okno.title("Edytuj pracownika" if edit_mode else "Dodaj pracownika")
        self.controller = controller
        self.edit_mode = edit_mode
        self.idx = idx

        Label(self.okno, text="Imię:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_imie = Entry(self.okno, width=30)
        self.entry_imie.grid(row=0, column=1, padx=5, pady=5)

        Label(self.okno, text="Nazwisko:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_nazwisko = Entry(self.okno, width=30)
        self.entry_nazwisko.grid(row=1, column=1, padx=5, pady=5)

        Label(self.okno, text="Restauracja:").grid(row=2, column=0, sticky="w", padx=5, pady=5)

        nazwy_restauracji = [r.nazwa for r in lista_restauracji]

        self.combo_restauracja = ttk.Combobox(
            self.okno,
            values=nazwy_restauracji,
            state="readonly",
            width=28
        )
        self.combo_restauracja.grid(row=2, column=1, padx=5, pady=5)

        if edit_mode and pracownik:
            self.entry_imie.insert(0, pracownik.imie)
            self.entry_nazwisko.insert(0, pracownik.nazwisko)
            if pracownik.restauracja in nazwy_restauracji:
                self.combo_restauracja.set(pracownik.restauracja)
            elif nazwy_restauracji:
                self.combo_restauracja.current(0)
        else:
            if nazwy_restauracji:
                self.combo_restauracja.current(0)
            else:
                self.combo_restauracja.config(state="disabled")

        Label(self.okno, text="Lat:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_lat = Entry(self.okno, width=30)
        self.entry_lat.grid(row=3, column=1, padx=5, pady=5)

        Label(self.okno, text="Lon:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_lon = Entry(self.okno, width=30)
        self.entry_lon.grid(row=4, column=1, padx=5, pady=5)

        if edit_mode and pracownik:
            self.entry_lat.insert(0, pracownik.lat)
            self.entry_lon.insert(0, pracownik.lon)

        btn_text = "Zapisz" if edit_mode else "Dodaj"
        Button(self.okno, text=btn_text, command=self.zapisz).grid(
            row=5, column=0, columnspan=2, pady=10
        )

    def zapisz(self):
        imie = self.entry_imie.get()
        nazwisko = self.entry_nazwisko.get()
        restauracja = self.combo_restauracja.get()
        lat = self.entry_lat.get()
        lon = self.entry_lon.get()

        if self.edit_mode:
            self.controller.edytuj(self.idx, imie, nazwisko, restauracja, lat, lon)
        else:
            self.controller.dodaj(imie, nazwisko, restauracja, lat, lon)

        self.okno.destroy()


class KlientForm:
    def __init__(self, parent, controller, edit_mode=False, idx=None, klient=None):
        self.okno = Toplevel(parent)
        self.okno.title("Edytuj klienta" if edit_mode else "Dodaj klienta")
        self.controller = controller
        self.edit_mode = edit_mode
        self.idx = idx

        Label(self.okno, text="Imię:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_imie = Entry(self.okno, width=30)
        self.entry_imie.grid(row=0, column=1, padx=5, pady=5)

        Label(self.okno, text="Nazwisko:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_nazwisko = Entry(self.okno, width=30)
        self.entry_nazwisko.grid(row=1, column=1, padx=5, pady=5)

        Label(self.okno, text="Restauracja:").grid(row=2, column=0, sticky="w", padx=5, pady=5)

        nazwy_restauracji = [r.nazwa for r in lista_restauracji]

        self.combo_restauracja = ttk.Combobox(
            self.okno,
            values=nazwy_restauracji,
            state="readonly",
            width=28
        )
        self.combo_restauracja.grid(row=2, column=1, padx=5, pady=5)

        if edit_mode and klient:
            self.entry_imie.insert(0, klient.imie)
            self.entry_nazwisko.insert(0, klient.nazwisko)
            if klient.restauracja in nazwy_restauracji:
                self.combo_restauracja.set(klient.restauracja)
            elif nazwy_restauracji:
                self.combo_restauracja.current(0)
        else:
            if nazwy_restauracji:
                self.combo_restauracja.current(0)
            else:
                self.combo_restauracja.config(state="disabled")

        Label(self.okno, text="Lat:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_lat = Entry(self.okno, width=30)
        self.entry_lat.grid(row=3, column=1, padx=5, pady=5)

        Label(self.okno, text="Lon:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_lon = Entry(self.okno, width=30)
        self.entry_lon.grid(row=4, column=1, padx=5, pady=5)

        if edit_mode and klient:
            self.entry_lat.insert(0, klient.lat)
            self.entry_lon.insert(0, klient.lon)

        btn_text = "Zapisz" if edit_mode else "Dodaj"
        Button(self.okno, text=btn_text, command=self.zapisz).grid(
            row=5, column=0, columnspan=2, pady=10
        )

    def zapisz(self):
        imie = self.entry_imie.get()
        nazwisko = self.entry_nazwisko.get()
        restauracja = self.combo_restauracja.get()
        lat = self.entry_lat.get()
        lon = self.entry_lon.get()

        if self.edit_mode:
            self.controller.edytuj(self.idx, imie, nazwisko, restauracja, lat, lon)
        else:
            self.controller.dodaj(imie, nazwisko, restauracja, lat, lon)

        self.okno.destroy()