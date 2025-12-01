from tkinter import *
from tkinter import ttk
from padg_lib import map_service
from padg_lib.model import *

# ===== USTAWIENIA OGÓLNE OKNA ===================================

BG = "#B8EDFD"       # tło aplikacji
PANEL_BG = "#92DCF2" # tło paneli
BTN_BG = "#e0e0e1"

root = Tk()
root.title("Jedzonko")
root.geometry("1220x960")
root.configure(bg=BG)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=2)

# ===== GÓRNY OBSZAR =============================================

top_frame = Frame(root, bg=BG)
top_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=20)

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)
top_frame.columnconfigure(3, weight=1)

# ===== DOLNY OBSZAR - MAPA ======================================

ramka_mapa = Frame(root, bg="#e0f7fa")
ramka_mapa.grid(row=1, column=0, columnspan=6, sticky="nsew", padx=15, pady=15)

map_widget = map_service.init_map(ramka_mapa)

# ===== FUNKCJE FORMULARZY =======================================

def formularz_restauracja():
    okno = Toplevel(root)
    okno.title("Dodaj restaurację")

    Label(okno, text="Nazwa:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_nazwa = Entry(okno, width=30)
    entry_nazwa.grid(row=0, column=1, padx=5, pady=5)

    Label(okno, text="Lat:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_lat = Entry(okno, width=30)
    entry_lat.grid(row=2, column=1, padx=5, pady=5)

    Label(okno, text="Lon:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_lon = Entry(okno, width=30)
    entry_lon.grid(row=3, column=1, padx=5, pady=5)

    def dodaj_restauracje():
        r = Restauracja(
            entry_nazwa.get(),
            entry_lat.get(),
            entry_lon.get()
        )
        lista_restauracji.append(r)
        listbox_lista_restauracji.insert(END, r.nazwa)
        map_service.add_marker(map_widget, float(r.lat), float(r.lon), r.nazwa)
        okno.destroy()

    Button(okno, text="Dodaj", command=dodaj_restauracje).grid(
        row=4, column=0, columnspan=2, pady=10
    )



def formularz_pracownik():
    okno = Toplevel(root)
    okno.title("Dodaj pracownika")

    Label(okno, text="Imię:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_imie = Entry(okno, width=30)
    entry_imie.grid(row=0, column=1, padx=5, pady=5)

    Label(okno, text="Nazwisko:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_nazwisko = Entry(okno, width=30)
    entry_nazwisko.grid(row=1, column=1, padx=5, pady=5)

    Label(okno, text="Restauracja:").grid(row=2, column=0, sticky="w", padx=5, pady=5)

    nazwy_restauracji = [r.nazwa for r in lista_restauracji]

    combo_restauracja = ttk.Combobox(
        okno,
        values=nazwy_restauracji,
        state="readonly",
        width=28
    )
    combo_restauracja.grid(row=2, column=1, padx=5, pady=5)

    if nazwy_restauracji:
        combo_restauracja.current(0)
    else:
        combo_restauracja.config(state="disabled")

    Label(okno, text="Lat:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_lat = Entry(okno, width=30)
    entry_lat.grid(row=3, column=1, padx=5, pady=5)

    Label(okno, text="Lon:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    entry_lon = Entry(okno, width=30)
    entry_lon.grid(row=4, column=1, padx=5, pady=5)

    def dodaj_pracownika():
        r = Pracownik(
            entry_imie.get(),
            entry_nazwisko.get(),
            combo_restauracja.get(),
            entry_lat.get(),
            entry_lon.get()
        )
        lista_pracownikow.append(r)
        listbox_lista_pracownikow.insert(END, f"{r.imie} {r.nazwisko} {r.restauracja}")
        map_service.add_marker(map_widget, float(r.lat), float(r.lon),f"{r.imie} {r.nazwisko}")
        okno.destroy()

    Button(okno, text="Dodaj", command=dodaj_pracownika).grid(
        row=5, column=0, columnspan=2, pady=10
    )


def formularz_klient():
    okno = Toplevel(root)
    okno.title("Dodaj klienta")

    Label(okno, text="Imię:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_imie = Entry(okno, width=30)
    entry_imie.grid(row=0, column=1, padx=5, pady=5)

    Label(okno, text="Nazwisko:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_nazwisko = Entry(okno, width=30)
    entry_nazwisko.grid(row=1, column=1, padx=5, pady=5)

    Label(okno, text="Restauracja:").grid(row=2, column=0, sticky="w", padx=5, pady=5)

    nazwy_restauracji = [r.nazwa for r in lista_restauracji]

    combo_restauracja = ttk.Combobox(
        okno,
        values=nazwy_restauracji,
        state="readonly",
        width=28
    )
    combo_restauracja.grid(row=2, column=1, padx=5, pady=5)

    if nazwy_restauracji:
        combo_restauracja.current(0)
    else:
        combo_restauracja.config(state="disabled")

    Label(okno, text="Lat:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    entry_lat = Entry(okno, width=30)
    entry_lat.grid(row=4, column=1, padx=5, pady=5)

    Label(okno, text="Lon:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
    entry_lon = Entry(okno, width=30)
    entry_lon.grid(row=5, column=1, padx=5, pady=5)

    def dodaj_klienta():
        r = Klient(
            entry_imie.get(),
            entry_nazwisko.get(),
            combo_restauracja.get(),
            entry_lat.get(),
            entry_lon.get()
        )
        lista_klientow.append(r)
        listbox_lista_klientow.insert(END, f"{r.imie} {r.nazwisko} {r.restauracja}")
        map_service.add_marker(map_widget, float(r.lat), float(r.lon),f"{r.imie} {r.nazwisko}")
        okno.destroy()

    Button(okno, text="Dodaj", command=dodaj_klienta).grid(
        row=6, column=0, columnspan=2, pady=10
    )


# ===== PANELE LIST =======================================


# --- Lista restauracji ---
ramka_lista_restauracji = LabelFrame(
    top_frame, text="Lista restauracji", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_restauracji.grid(row=0, column=0, sticky="nsew", padx=10)

listbox_lista_restauracji = Listbox(ramka_lista_restauracji, width=25, height=15)
listbox_lista_restauracji.grid(row=0, column=0, columnspan=3, pady=(0, 10))

button_restauracja_szczegoly = Button(ramka_lista_restauracji, text="Szczegóły", bg=BTN_BG)
button_restauracja_szczegoly.grid(row=1, column=0, padx=2)

button_restauracja_edytuj = Button(ramka_lista_restauracji, text="Edytuj", bg=BTN_BG)
button_restauracja_edytuj.grid(row=1, column=1, padx=2)

button_restauracja_usun = Button(ramka_lista_restauracji, text="Usuń", bg=BTN_BG)
button_restauracja_usun.grid(row=1, column=2, padx=2)


# --- Lista pracowników ---
ramka_lista_pracownikow = LabelFrame(
    top_frame, text="Lista pracowników", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_pracownikow.grid(row=0, column=1, sticky="nsew", padx=10)

listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow, width=25, height=15)
listbox_lista_pracownikow.grid(row=0, column=0, columnspan=3, pady=(0, 10))

button_pracownik_szczegoly = Button(ramka_lista_pracownikow, text="Szczegóły", bg=BTN_BG)
button_pracownik_szczegoly.grid(row=1, column=0, padx=2)

button_pracownik_edytuj = Button(ramka_lista_pracownikow, text="Edytuj", bg=BTN_BG)
button_pracownik_edytuj.grid(row=1, column=1, padx=2)

button_pracownik_usun = Button(ramka_lista_pracownikow, text="Usuń", bg=BTN_BG)
button_pracownik_usun.grid(row=1, column=2, padx=2)


# --- Lista klientów ---
ramka_lista_klientow = LabelFrame(
    top_frame, text="Lista klientów", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_klientow.grid(row=0, column=2, sticky="nsew", padx=10)

listbox_lista_klientow = Listbox(ramka_lista_klientow, width=25, height=15)
listbox_lista_klientow.grid(row=0, column=0, columnspan=3, pady=(0, 10))

button_klient_szczegoly = Button(ramka_lista_klientow, text="Szczegóły", bg=BTN_BG)
button_klient_szczegoly.grid(row=1, column=0, padx=2)

button_klient_edytuj = Button(ramka_lista_klientow, text="Edytuj", bg=BTN_BG)
button_klient_edytuj.grid(row=1, column=1, padx=2)

button_klient_usun = Button(ramka_lista_klientow, text="Usuń", bg=BTN_BG)
button_klient_usun.grid(row=1, column=2, padx=2)


# --- Panel formularzy ---
ramka_formularz = LabelFrame(
    top_frame, text="Formularze", bg=PANEL_BG, padx=10, pady=10
)
ramka_formularz.grid(row=0, column=3, sticky="n", padx=10)

button_dodaj_restauracje = Button(
    ramka_formularz, text="Dodaj restaurację", width=18, command=formularz_restauracja, bg=BTN_BG
)
button_dodaj_restauracje.grid(row=0, column=0, pady=5)

button_dodaj_pracownika = Button(
    ramka_formularz, text="Dodaj pracownika", width=18, command=formularz_pracownik, bg=BTN_BG
)
button_dodaj_pracownika.grid(row=1, column=0, pady=5)

button_dodaj_klienta = Button(
    ramka_formularz, text="Dodaj klienta", width=18, command=formularz_klient, bg=BTN_BG
)
button_dodaj_klienta.grid(row=2, column=0, pady=5)


root.mainloop()
