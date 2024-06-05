import random
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")
character_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password_gen = ctk.CTk()
password_gen.geometry("400x250")
password_gen.title("Password Generator")
