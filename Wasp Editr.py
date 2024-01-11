import subprocess
import tkinter as tk
from tkinter import filedialog
import pdb

root = tk.Tk()
root.title("Wasp Editr")

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".wmf" or ".html" or ".css" or ".pdf" or ".txt" or ".sh" or ".bash" or ".py")
    if file is None:
        return
    text = str(text_editor.get(1.0, tk.END))
    file.write(text)
    file.close()

def html_file():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, "<!DOCTYPE html>\n<html>\n<head>\n<title>My HTML File</title>\n</head>\n<body>\n\n</body>\n</html>")

def css_file():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, "/* Add your CSS code here */")

def new_file():
    text_editor.delete(1.0, tk.END)

def available_extensions():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, ".wmf, .html, .css, .pdf(still in developement), .txt, .sh, .bash(same as .sh)")

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is None:
        return
    text = file.read()
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, text)
    file.close()

text_editor = tk.Text(root)
text_editor.pack()

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack()

new_button = tk.Button(root, text="New", command=new_file)
new_button.pack()

html_button = tk.Button(root, text="HTML DOC", command=html_file)
html_button.pack()

css_button = tk.Button(root, text="CSS FILE", command=css_file)
css_button.pack()

extensions_button = tk.Button(root, text="Available Extensions", command=available_extensions)
extensions_button.pack()

import tkinter as tk

def encrypt_text():
    text = text_editor.get("1.0", "end-1c")
    encrypted_text = "".join([str(ord(char)) for char in text])
    text_editor.delete("1.0", "end")
    text_editor.insert("1.0", encrypted_text)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

root.mainloop()
























