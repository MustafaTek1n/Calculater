import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# Fonksiyonlar
def pdf_sec():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, file_path)

def ara():

    pdf_path = entry_pdf.get()
    aranan_kelime = entry_string.get().strip()
    if not pdf_path or not aranan_kelime:
        messagebox.showwarning("Uyarı", "PDF ve aranacak kelimeyi girin!")
        return

    try:
        pdf_file = open(pdf_path, "rb")
        reader = PyPDF2.PdfReader(pdf_file)
        bulunan_sayfalar = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and aranan_kelime.lower() in text.lower():
                bulunan_sayfalar.append(i+1)  # Sayfa numarası 1'den başlasın

        pdf_file.close()

        if bulunan_sayfalar:
            result_label.config(text=f"'{aranan_kelime}' bulunduğu sayfalar: {bulunan_sayfalar}")
        else:
            result_label.config(text=f"'{aranan_kelime}' bulunamadı.")

    except Exception as e:
        messagebox.showerror("Hata", f"PDF okunamadı: {e}")

# GUI
root = tk.Tk()
root.title("PDF Arama")

tk.Label(root, text="PDF Dosyası:").grid(row=0, column=0, padx=5, pady=5)
entry_pdf = tk.Entry(root, width=50)
entry_pdf.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Seç", command=pdf_sec).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Aranacak Kelime:").grid(row=1, column=0, padx=5, pady=5)
entry_string = tk.Entry(root, width=50)
entry_string.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Ara", command=ara).grid(row=2, column=1, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
