import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
from tkinter import Tk, Text, Menu, StringVar, OptionMenu

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Yeni Dosya - Text Editor")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
            root.title(f"{file_path} - Text Editor")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya Açılamadı: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Text Editor")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya Kaydedilemedi: {e}")


def exit_editor():
    if  messagebox.askokcancel("Çıkış", "Çıkmak İstediğinize Emin Misiniz? Kaydetmeyi Unutmayın."):
        root.destroy()

def exit_editor2():
    if  messagebox.askokcancel("Çıkış", "Çıkmak İstediğinize Emin Misiniz?"):
        root.destroy()

def saveandexit():
    save_file()
    exit_editor2()

def open_python():
    webbrowser.open("https://www.python.org/")

def open_python_download():
    webbrowser.open("https://www.python.org/downloads/")
    
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def about():
    messagebox.showinfo("Hakkında", "Text Editor v1.0\nDoruk Eren Şimşek\nPython3\nVS Code")

def update_font(*args):
    font_family = current_font_family.get()
    font_size = int(current_font_size.get())
    text_area.config(font=(font_family, font_size))
    
def find_and_replace():
    def replace_text():
        find_text = find_entry.get()
        replace_text = replace_entry.get()
        content = text_area.get(1.0, tk.END)
        new_content = content.replace(find_text, replace_text)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, new_content)

    replace_window = tk.Toplevel(root)
    replace_window.title("Bul ve Değiştir")

    tk.Label(replace_window, text="Bul:").grid(row=0, column=0, padx=5, pady=5)
    find_entry = tk.Entry(replace_window)
    find_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(replace_window, text="Değiştir:").grid(row=1, column=0, padx=5, pady=5)
    replace_entry = tk.Entry(replace_window)
    replace_entry.grid(row=0, column=1, padx=5, pady=5)

root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

current_font_family = StringVar(value="Arial")
current_font_size = StringVar(value="12")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Yeni", command=new_file)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Kapat", command=exit_editor)
file_menu.add_command(label="Kaydet ve Kapat", command=saveandexit)
file_menu.add_command(label="Python", command=open_python)
file_menu.add_command(label="Python İndir", command=open_python_download)
menu_bar.add_cascade(label="Dosya", menu=file_menu)

dedit_menu = tk.Menu(menu_bar, tearoff=0)
dedit_menu.add_command(label="Kes", command=cut_text)
dedit_menu.add_command(label="Kopyala", command=copy_text)
dedit_menu.add_command(label="Yapıştır", command=paste_text)
menu_bar.add_cascade(label="Düzen", menu=dedit_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hakkında", command=about)
menu_bar.add_cascade(label="Yardım", menu=help_menu)

font_menu = tk.Menu(menu_bar, tearoff=0)
font_families = ["Arial", "Times New Roman", "Courier New", "Comic Sans MS"]
font_sizes = [str(size) for size in range(8, 33, 2)]

font_family_menu = tk.Menu(font_menu, tearoff=0)
for font in font_families:
    font_family_menu.add_radiobutton(label=font, variable=current_font_family, command=update_font)
font_menu.add_cascade(label="Yazı Tipi", menu=font_family_menu)

menu_bar.add_cascade(label="Yazı", menu=font_menu)

font_size_menu = tk.Menu(font_menu, tearoff=0)
for size in font_sizes:
    font_size_menu.add_radiobutton(label=size, variable=current_font_size, command=update_font)
font_menu.add_cascade(label="Yazı Boyutu", menu=font_size_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root, font=("Arial", 14))
text_area.pack(expand=True, fill=tk.BOTH)

root.protocol("WM_DELETE_WINDOW", exit_editor)
root.mainloop()
