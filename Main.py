import customtkinter as ctk
import tkinter.messagebox as tkmb
import subprocess

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1280x720")
app.title("WhiteArchTech")

class BoxFrame(ctk.CTkFrame):
    def __init__(self, master, title, size):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=5)

        self.title_label = ctk.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.configure(width=size, height=size)
        self.grid_propagate(False)

        self.news_container = ctk.CTkFrame(self) # Container for news items
        self.news_container.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.news_container.grid_columnconfigure(0, weight=1)

    def add_news_items(self, news_text):
        news_label = ctk.CTkLabel(self.news_container, text=news_text, fg_color="gray20", corner_radius=6)
        news_label.grid(row=self.news_container.grid_size()[1], column=0, padx=10, pady=(5, 5), sticky="ew")

welcome_label = ctk.CTkLabel(app, text="Welcome to WhiteArchTech!\nThis application is base on CyberWhiteArch. \nIt's totally privacy-focused and open-source virus and hash scanner.", fg_color="transparent", bg_color='transparent', corner_radius=6)
welcome_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
welcome_label.configure(font=("Helvetica", 20, "bold"))
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

frame = BoxFrame(app, title="Annoucement", size=450)
frame.grid(row=1, column=0, padx=20, pady=20)

def open_hash_generator():
    subprocess.Popen(["python", "hashgenerator.py"])

open_scan_button = ctk.CTkButton(app, text="Generator Hash", command=open_hash_generator)
open_scan_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()