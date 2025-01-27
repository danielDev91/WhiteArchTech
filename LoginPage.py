#This is a test for login interface for python this app doesnt requires login its total privacy.
import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

def login():
    username = "AdminDaniel"
    password = "@dan!l3"

    # adding if statement 
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='wrong Username', message='Please check your username')
    else:
        tkmb.showerror(title="login failed", message="Invalid Username or Password")

label = ctk.CTkLabel(app, text="This is the main UI Page under construction")

label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Moden Login System UI')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login')
button.pack(pady=10, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

app.mainloop()
