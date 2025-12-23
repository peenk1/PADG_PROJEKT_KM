from tkinter import *
from padg_lib import map_service
from padg_lib.model import lista_restauracji, lista_pracownikow, lista_klientow
from padg_lib.controller import RestauracjaController, PracownikController, KlientController
from padg_lib.forms import RestauracjaForm, PracownikForm, KlientForm

# ===== USTAWIENIA OGÓLNE OKNA =======

BG = "#B8EDFD"
PANEL_BG = "#92DCF2"
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

# ===== GÓRNY OBSZAR ========

top_frame = Frame(root, bg=BG)
top_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=20)

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)
top_frame.columnconfigure(3, weight=1)

# ===== DOLNY OBSZAR - MAPA ========

ramka_mapa = Frame(root, bg="#e0f7fa")
ramka_mapa.grid(row=1, column=0, columnspan=6, sticky="nsew", padx=15, pady=15)

map_widget = map_service.init_map(ramka_mapa)

# ===== PANELE LIST =======

# --- Lista restauracji ---
ramka_lista_restauracji = LabelFrame(
    top_frame, text="Lista restauracji", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_restauracji.grid(row=0, column=0, sticky="nsew", padx=10)

listbox_lista_restauracji = Listbox(ramka_lista_restauracji, width=25, height=15)
listbox_lista_restauracji.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# --- Lista pracowników ---
ramka_lista_pracownikow = LabelFrame(
    top_frame, text="Lista pracowników", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_pracownikow.grid(row=0, column=1, sticky="nsew", padx=10)

listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow, width=25, height=15)
listbox_lista_pracownikow.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# --- Lista klientów ---
ramka_lista_klientow = LabelFrame(
    top_frame, text="Lista klientów", bg=PANEL_BG, padx=10, pady=10
)
ramka_lista_klientow.grid(row=0, column=2, sticky="nsew", padx=10)

listbox_lista_klientow = Listbox(ramka_lista_klientow, width=25, height=15)
listbox_lista_klientow.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# ======= KONTROLERY ========

restauracja_ctrl = RestauracjaController(
    map_widget,
    listbox_lista_restauracji,
    listbox_lista_pracownikow,
    listbox_lista_klientow
)

pracownik_ctrl = PracownikController(map_widget, listbox_lista_pracownikow)
klient_ctrl = KlientController(map_widget, listbox_lista_klientow)

# ======= FUNKCJE CALLBACKS ==============

# Restauracje
def dodaj_restauracje():
    RestauracjaForm(root, restauracja_ctrl)

def edytuj_restauracje():
    idx = listbox_lista_restauracji.curselection()
    if idx:
        idx = idx[0]
        RestauracjaForm(root, restauracja_ctrl, edit_mode=True, idx=idx, restauracja=lista_restauracji[idx])

def usun_restauracje():
    idx = listbox_lista_restauracji.curselection()
    if idx:
        restauracja_ctrl.usun(idx[0])

def szczegoly_restauracji():
    idx = listbox_lista_restauracji.curselection()
    if idx:
        restauracja_ctrl.pokaz_na_mapie(idx[0])

# Pracownicy
def dodaj_pracownika():
    PracownikForm(root, pracownik_ctrl)

def edytuj_pracownika():
    idx = listbox_lista_pracownikow.curselection()
    if idx:
        idx = idx[0]
        PracownikForm(root, pracownik_ctrl, edit_mode=True, idx=idx, pracownik=lista_pracownikow[idx])

def usun_pracownika():
    idx = listbox_lista_pracownikow.curselection()
    if idx:
        pracownik_ctrl.usun(idx[0])

def szczegoly_pracownika():
    idx = listbox_lista_pracownikow.curselection()
    if idx:
        pracownik_ctrl.pokaz_na_mapie(idx[0])

# Klienci
def dodaj_klienta():
    KlientForm(root, klient_ctrl)

def edytuj_klienta():
    idx = listbox_lista_klientow.curselection()
    if idx:
        idx = idx[0]
        KlientForm(root, klient_ctrl, edit_mode=True, idx=idx, klient=lista_klientow[idx])

def usun_klienta():
    idx = listbox_lista_klientow.curselection()
    if idx:
        klient_ctrl.usun(idx[0])

def szczegoly_klienta():
    idx = listbox_lista_klientow.curselection()
    if idx:
        klient_ctrl.pokaz_na_mapie(idx[0])

# ===== PRZYCISKI ======

# Przyciski restauracji
Button(ramka_lista_restauracji, text="Szczegóły", bg=BTN_BG, command=szczegoly_restauracji).grid(row=1, column=0, padx=2)
Button(ramka_lista_restauracji, text="Edytuj", bg=BTN_BG, command=edytuj_restauracje).grid(row=1, column=1, padx=2)
Button(ramka_lista_restauracji, text="Usuń", bg=BTN_BG, command=usun_restauracje).grid(row=1, column=2, padx=2)

# Przyciski pracowników
Button(ramka_lista_pracownikow, text="Szczegóły", bg=BTN_BG, command=szczegoly_pracownika).grid(row=1, column=0, padx=2)
Button(ramka_lista_pracownikow, text="Edytuj", bg=BTN_BG, command=edytuj_pracownika).grid(row=1, column=1, padx=2)
Button(ramka_lista_pracownikow, text="Usuń", bg=BTN_BG, command=usun_pracownika).grid(row=1, column=2, padx=2)

# Przyciski klientów
Button(ramka_lista_klientow, text="Szczegóły", bg=BTN_BG, command=szczegoly_klienta).grid(row=1, column=0, padx=2)
Button(ramka_lista_klientow, text="Edytuj", bg=BTN_BG, command=edytuj_klienta).grid(row=1, column=1, padx=2)
Button(ramka_lista_klientow, text="Usuń", bg=BTN_BG, command=usun_klienta).grid(row=1, column=2, padx=2)

# --- Panel formularzy ---
ramka_formularz = LabelFrame(
    top_frame, text="Formularze", bg=PANEL_BG, padx=10, pady=10
)
ramka_formularz.grid(row=0, column=3, sticky="n", padx=10)

Button(ramka_formularz, text="Dodaj restaurację", width=18, command=dodaj_restauracje, bg=BTN_BG).grid(row=0, column=0, pady=5)
Button(ramka_formularz, text="Dodaj pracownika", width=18, command=dodaj_pracownika, bg=BTN_BG).grid(row=1, column=0, pady=5)
Button(ramka_formularz, text="Dodaj klienta", width=18, command=dodaj_klienta, bg=BTN_BG).grid(row=2, column=0, pady=5)

def run_app():
    root.mainloop()
