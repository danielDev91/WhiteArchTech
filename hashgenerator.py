# Page to scan hashes
import customtkinter as ctk
import hashlib
import requests
from tkinter import filedialog


ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

def generate_hash(text, algorithm):
    if algorithm == "MD5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "SHA1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "SHA256":
        return hashlib.sha256(text.encode()).hexdigest()
    return None

def open_hash_page():
    scan_app = ctk.CTk()
    scan_app.geometry("1280x720")
    scan_app.title("Hash Generator")

    welcome_label = ctk.CTkLabel(scan_app, text="Text convert to hash", font=("Helvetica", 20, "bold"))
    welcome_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    scan_app.grid_rowconfigure(0, weight=1)
    scan_app.grid_columnconfigure(0, weight=1)

    # ======== HASH GENERATOR ======== #
    text_entry = ctk.CTkEntry(scan_app, placeholder_text="Enter text to hash")
    text_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    algorithm_var = ctk.StringVar(value="MD5")
    algorithm_menu = ctk.CTkOptionMenu(scan_app, variable=algorithm_var, values=["MD5", "SHA1", "SHA256"])
    algorithm_menu.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    result_label = ctk.CTkLabel(scan_app, text="")
    result_label.grid(row=4, column=0, padx=10, pady=10, stick="nsew")

    def on_hash_button_click():
        text = text_entry.get()
        algorithm = algorithm_var.get()
        hashed_text = generate_hash(text, algorithm)
        result_label.configure(text=f'hashed Text ({algorithm}) : {hashed_text}')
    
    hash_button = ctk.CTkButton(scan_app, text="Generate Hash", command=on_hash_button_click)
    hash_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    # ======= VIRUS SCAN VIA API VIRUS TOTAL ======== #
    file_label = ctk.CTkLabel(scan_app, text="Choose a file to scan", font=("Helvetica", 18, "bold"))
    file_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    file_path_label = ctk.CTkLabel(scan_app, text="")
    file_path_label.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

    def choose_file():
        file_path = filedialog.askopenfilename()
        file_path_label.configure(text=f"selected File: {file_path}")
        return file_path


    scan_app.mainloop()
    
if __name__ == "__main__":
    open_hash_page()