import customtkinter as ctk

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

def open_scan_page():
    scan_app = ctk.CTk()
    scan_app.geometry("1280x720")
    scan_app.title("Scan Page")

    welcome_label = ctk.CTkLabel(scan_app, text="Welcome to the scan page", font=("Helvetica", 20, "bold"))
    welcome_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    scan_app.grid_rowconfigure(0, weight=1)
    scan_app.grid_columnconfigure(0, weight=1)

    scan_app.mainloop()

if __name__ == "__main__":
    open_scan_page()