import random
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")
character_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password_gen = ctk.CTk()
password_gen.geometry("400x250")
password_gen.title("Password Generator")
def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror(message="Please key in the required inputs")
        return

    if repeat == 1:
        password = ''.join(random.sample(character_string, length))
    else:
        password = ''.join(random.choices(character_string, k=length))
    
    password_v.set("Created password: " + password)

def copy_password():
    password_gen.clipboard_clear()
    password_gen.clipboard_append(password_v.get().replace("Created password: ", ""))
    messagebox.showinfo(message="Password copied to clipboard!")

length_label = ctk.CTkLabel(password_gen, text="Length of password:")
length_label.place(x=10, y=10)
length_entry = ctk.CTkEntry(password_gen)
length_entry.place(x=230, y=10)

repeat_label = ctk.CTkLabel(password_gen, text="Unique characters (1: Yes, 0: No):")
repeat_label.place(x=10, y=50)
repeat_entry = ctk.CTkEntry(password_gen)
repeat_entry.place(x=230, y=50)

generate_button = ctk.CTkButton(password_gen, text="Generate Password", command=generate_password)
generate_button.place(x=10, y=90)



