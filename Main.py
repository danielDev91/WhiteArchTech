import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import Menu

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1280x720")
app.title("WhiteArchTech")

menubar = Menu(app)
app.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label='Login')
file_menu.add_command(label='Return')
file_menu.add_command(label='Close Page') #Adding the command to close the page only not the main
file_menu.add_separator()

#Adding the files and pages

file_menu.add_command(
    label='Exit',
    command=app.destroy
)

menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

menubar.add_cascade(
    label='Help',
    menu=help_menu
)

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

frame = BoxFrame(app, title="News", size=450)
frame.grid(row=1, column=0, padx=20, pady=20)
frame.add_news_items("Breaking news: AI Companions getting more conversation")
frame.add_news_items("Update : New features will be added to the application.")
frame.add_news_items("Announcement: Upcoming interface on WhiteArchTech")

app.mainloop()