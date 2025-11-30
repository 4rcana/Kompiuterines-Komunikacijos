import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Globalios konstantos skirtos duomenų bazės prisijungimui
DATABASE_NAME = "ld3"
DATABASE_TABLE_NAME = "devboard_data"

# Prisijungti prie duomenų bazės
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=DATABASE_NAME
    )

# Funkcija rašyti duomenims į duomenų bazę
# Aktyvuojama paspaudus `Įrašyti į duomenų bazę` mygtuką
def write_to_db():
    global entry_koordinates, entry_laikas, entry_palydovai, entry_temperatura
    koordinates = entry_koordinates.get()
    laikas = entry_laikas.get()
    palydovai = int(entry_palydovai.get())
    temperatura = float(entry_temperatura.get())

    if koordinates and laikas and (palydovai >= 0) and temperatura:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {DATABASE_TABLE_NAME} "
                       f"(temperatura, koordinates, laikas, palydovai) "
                       f"VALUES (%s, %s, %s, %s)",
                       (temperatura, koordinates, laikas, palydovai))
        conn.commit()
        cursor.close()
        conn.close()
        entry_koordinates.delete(0, tk.END)
        entry_laikas.delete(0, tk.END)
        entry_palydovai.delete(0, tk.END)
        entry_temperatura.delete(0, tk.END)
        messagebox.showinfo("Sėkmė", "Duomenys įrašyti į duomenų bazę")
    else:
        messagebox.showwarning("Klaida", "Prašome įrašyti tekstą")

# Funkcija skaityti duomenis iš duomenų bazės ir juos atvaizduoti `text_display` teksto lauke
# Aktyvuojama paspaudus `Skaityti iš duomenų bazės` mygtuką
def read_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT temperatura, koordinates, laikas, palydovai "
                   f"FROM {DATABASE_TABLE_NAME}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Atvaizduoti tekstiniame lauke
    display_text = "\n".join(str(row) for row in rows)
    text_display.config(state=tk.NORMAL)
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, display_text)
    text_display.config(state=tk.DISABLED)

# Pagrindinio lango kūrimas
root = tk.Tk()
root.title("Kompiuterinės Komunikacijos 3 Lab. Darbas")
root.grid_rowconfigure(11, weight=1)
root.grid_columnconfigure(0, weight=1)

# Vizualinių elementų kūrimas
tk.Label(root, text="Įrašyti koordinates:").grid(row=1, column=0, padx=10, pady=10)
entry_koordinates = tk.Entry(root, width=50)
entry_koordinates.grid(row=2, column=0, padx=10, pady=10)

tk.Label(root, text="Įrašyti laiką:").grid(row=3, column=0, padx=10, pady=10)
entry_laikas = tk.Entry(root, width=50)
entry_laikas.grid(row=4, column=0, padx=10, pady=10)

tk.Label(root, text="Įrašyti palydovų skaičių:").grid(row=5, column=0, padx=10, pady=10)
entry_palydovai = tk.Entry(root, width=50)
entry_palydovai.grid(row=6, column=0, padx=10, pady=10)

tk.Label(root, text="Įrašyti temperatūrą:").grid(row=7, column=0, padx=10, pady=10)
entry_temperatura = tk.Entry(root, width=50)
entry_temperatura.grid(row=8, column=0, padx=10, pady=10)


tk.Button(root, text="Įrašyti į duomenų bazę", command=write_to_db).grid(row=9, column=0, padx=10, pady=10)
tk.Button(root, text="Skaityti iš duomenų bazės", command=read_from_db).grid(row=10, column=0, padx=10, pady=10)

text_display = tk.Text(root, width=60, height=15, state=tk.DISABLED)
text_display.grid(row=11, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()
