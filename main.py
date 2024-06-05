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