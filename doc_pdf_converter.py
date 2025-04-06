import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
from pdf2docx import Converter
import os

class DocumentConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Belge Dönüştürücü")
        self.window.geometry("400x300")
        self.window.configure(bg="#f0f0f0")

        # Ana başlık
        tk.Label(self.window, text="Belge Dönüştürücü", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

       
        self.conversion_type = tk.StringVar(value="doc2pdf")
        tk.Radiobutton(self.window, text="WORD -> PDF ", variable=self.conversion_type, 
                      value="doc2pdf", bg="#f0f0f0").pack(pady=5)
        tk.Radiobutton(self.window, text="PDF -> WORD", variable=self.conversion_type, 
                      value="pdf2doc", bg="#f0f0f0").pack(pady=5)

      
        tk.Button(self.window, text="Dosya Seç", command=self.select_file,
                 bg="#4CAF50", fg="white", width=20).pack(pady=20)

    def select_file(self):
        file_types = []
        if self.conversion_type.get() == "doc2pdf":
            file_types = [("Word Dosyası", "*.docx"), ("Word Dosyası", "*.doc")]
        else:
            file_types = [("PDF Dosyası", "*.pdf")]

        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            self.convert_file(file_path)

    def convert_file(self, input_file):
        try:
            if self.conversion_type.get() == "doc2pdf":
                output_file = os.path.splitext(input_file)[0] + ".pdf"
                convert(input_file, output_file)
                messagebox.showinfo("Başarılı", "DOC dosyası PDF'e dönüştürüldü!")
            else:
                output_file = os.path.splitext(input_file)[0] + ".docx"
                cv = Converter(input_file)
                cv.convert(output_file)
                cv.close()
                messagebox.showinfo("Başarılı", "PDF dosyası DOC'a dönüştürüldü!")
        except Exception as e:
            messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu:\n{str(e)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DocumentConverter()
    app.run() 