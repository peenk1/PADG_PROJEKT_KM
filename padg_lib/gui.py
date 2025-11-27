from tkinter import *

root = Tk()
root.title("Jedzonko")
root.geometry("1920x1080")

ramka_lista_restauracji = Frame(root)
ramka_lista_pracownikow = Frame(root)
ramka_lista_klientow = Frame(root)
ramka_formularz = Frame(root)

ramka_lista_restauracji.grid(row=0, column=0)
ramka_lista_pracownikow.grid(row=0, column=1)
ramka_lista_klientow.grid(row=0, column=2)
ramka_formularz.grid(row=0, column=3)

# RAMKA LISTA RESTAURACJI

label_lista_restauracji = Label(ramka_lista_restauracji, text="Lista Restauracji")
label_lista_restauracji.grid(row=0, column=0)

listbox_lista_restauracji = Listbox(ramka_lista_restauracji)
listbox_lista_restauracji.grid(row=1, column=0)

button_restauracja_szczegoly = Button(ramka_lista_restauracji, text="Pokaż Szczegóły")
button_restauracja_szczegoly.grid(row=2, column=0)

button_restauracja_usun = Button(ramka_lista_restauracji, text="Usuń")
button_restauracja_usun.grid(row=2, column=1)

button_restauracja_edytuj = Button(ramka_lista_restauracji, text="Edytuj")
button_restauracja_edytuj.grid(row=2, column=2)

# RAMKA LISTA PRACOWNIKÓW

label_lista_pracownikow = Label(ramka_lista_pracownikow, text="Lista Pracownikow")
label_lista_pracownikow.grid(row=0, column=0)

listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow)
listbox_lista_pracownikow.grid(row=1, column=0)

button_pracownik_szczegoly = Button(ramka_lista_pracownikow, text="Pokaż Szczegóły")
button_pracownik_szczegoly.grid(row=2, column=0)

button_pracownik_usun = Button(ramka_lista_pracownikow, text="Usuń")
button_pracownik_usun.grid(row=2, column=1)

button_pracownik_edytuj = Button(ramka_lista_pracownikow, text="Edytuj")
button_pracownik_edytuj.grid(row=2, column=2)

# RAMKA LISTA KLIENTOW

label_lista_klientow = Label(ramka_lista_klientow, text="Lista Pracownikow")
label_lista_klientow.grid(row=0, column=0)

listbox_lista_klientow = Listbox(ramka_lista_klientow)
listbox_lista_klientow.grid(row=1, column=0)

button_klient_szczegoly = Button(ramka_lista_klientow, text="Pokaż Szczegóły")
button_klient_szczegoly.grid(row=2, column=0)

button_klient_usun = Button(ramka_lista_klientow, text="Usuń")
button_klient_usun.grid(row=2, column=1)

button_klient_edytuj = Button(ramka_lista_klientow, text="Edytuj")
button_klient_edytuj.grid(row=2, column=2)

# RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=3, columnspan=2)

button_dodaj_restauracje = Button(ramka_formularz, text="Dodaj restauracje")
button_dodaj_restauracje.grid(row=1, column=0)

button_dodaj_pracownika = Button(ramka_formularz, text="Dodaj pracownika")
button_dodaj_pracownika.grid(row=1, column=1)

button_dodaj_klienta = Button(ramka_formularz, text="Dodaj klienta")
button_dodaj_klienta.grid(row=1, column=2)

# RAMKA SZCZEGOLY





root.mainloop()
