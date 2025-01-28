import customtkinter 
import os
from PIL import Image

class Test(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")

        customtkinter.set_default_color_theme("blue")
        
        self.title("image_exemple.py")
        self.geometry("700x450")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Image Exemple", compound="left", font=customtkinter.CTkFont(size=15, weight="bold")) #image= 'something or a logo'
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")
    
if __name__=="__main__":
    test = Test()
    test.mainloop()