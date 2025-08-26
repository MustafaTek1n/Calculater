import tkinter as tk
from functools import partial

class Calculator:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.label = tk.Label(self.root, text="Calculate", font=("Arial", 24))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=("Arial", 20), height=2)
        self.textbox.pack(padx=10, pady=10, fill="x")

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.pack(fill="both", expand=True)

        # Ortak fonksiyonlar
        def buton_basil(char):
            self.textbox.insert(tk.END, str(char))

        def temizle():
            self.textbox.delete("1.0", tk.END)

        def backspace():
            icerik = self.textbox.get("1.0", "end-1c")  # sondaki \n hariç al
            if len(icerik) > 0:
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert("1.0", icerik[:-1])  # son karakteri sil

        def esittir():
            try:
                ifade = self.textbox.get("1.0", "end-1c")
                allowed = set("0123456789+-*/.%() ")
                if all(ch in allowed for ch in ifade):
                    sonuc = str(eval(ifade))
                    self.textbox.delete("1.0", tk.END)
                    self.textbox.insert(tk.END, sonuc)
                else:
                    raise ValueError("Geçersiz karakter")
            except ZeroDivisionError:
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert(tk.END, "Sıfıra bölünmez kanka")
            except SyntaxError:
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert(tk.END, "İfade bozuk")
            except Exception:
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert(tk.END, "Error")


        butonlar = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("←", 5, 1)
        ]

        for (text, row, col) in butonlar:
            if text == "=":
                btn = tk.Button(self.buttonFrame, text=text, font=("Arial", 20),command=esittir)
            elif text == "C":
                btn = tk.Button(self.buttonFrame, text=text, font=("Arial", 20),command=temizle)
            elif text == "←":
                btn = tk.Button(self.buttonFrame, text=text, font=("Arial", 20),command=backspace)
            else:
                #partial methodu ile buton_basil fonksiyonuna text parametresini geçiyoruz
                btn = tk.Button(self.buttonFrame, text=text, font=("Arial", 20),command=partial(buton_basil, text))

            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Tüm sütun ve satırları eşit genişlikte yap
        for i in range(4):
            self.buttonFrame.columnconfigure(i, weight=1)
        for i in range(6):
            self.buttonFrame.rowconfigure(i, weight=1)

        self.root.mainloop()

Calculator()
