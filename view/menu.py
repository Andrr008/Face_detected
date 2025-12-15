import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image


def menu():
# Configurasi Window
    from input import opencv
    from detect import detect_face

    # ===== PATH FIX =====
    VIEW_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(VIEW_DIR)

    ICON_PATH = os.path.join(BASE_DIR, "icon.ico")
    IMAGE_PATH = os.path.join(BASE_DIR, "face-recognition.png")

    app = ctk.CTk()
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    app.title("Face Detection")
    app.iconbitmap(ICON_PATH)

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}+-10+0")

    frame = ctk.CTkFrame(
        app,
        width=screen_width,
        height=screen_height * 0.4,
        fg_color=app._fg_color
    )
    frame.pack(pady=80)

    image = ctk.CTkImage(Image.open(IMAGE_PATH), size=(150, 150))
    label = ctk.CTkLabel(frame, image=image, text="")
    label.pack(side="left", padx=30, pady=20)

    texts = ["Face Recognition", "With DeepFace", "Use ArcFace Model"]
    label_font = ctk.CTkLabel(frame, text="", font=("Tahoma", 90, "bold"))
    label_font.pack(side="left", padx=10, pady=20)

    index = 0
    text_index = 0
    typing = True
    
    def animate():
        nonlocal index, typing, text_index
        current_text = texts[text_index]
    
        if typing:
            index += 1
            label_font.configure(text=current_text[:index])
            if index >= len(current_text):
                typing = False
                app.after(1500, animate)  # tunggu sebelum menghapus
                return
        else:
            index -= 1
            label_font.configure(text=current_text[:index])
            if index <= 0:
                typing = True
                text_index = (text_index + 1) % len(texts)
                app.after(500, animate)  # tunggu sebelum mengetik ulang
                return
    
        app.after(100, animate)
    
    # Mulai animasi
    animate()
    
    
    # membuat tampilan menu
    def input():
        new = opencv()
        print (new)
    
    def detect():
        new = detect_face()
        print (new)
    
    menu = ["New➕", "Detect🔎", "Users👥","History⌛"]
    commandMenu = [input, detect, "", ""]
    i = 0
    for i in range(len(menu)):
        newMenu = ctk.CTkButton(app, text=menu[i], command= commandMenu[i])
        newMenu.configure(height = 230, width = 230, font = ("Arial",30,"bold"), cursor = "hand2")
        newMenu.pack(side = "left", anchor = "sw", padx = 45, pady = 100)
        i+=1
    
    
    
    app.mainloop()

if __name__ == "__main__":
    menu()