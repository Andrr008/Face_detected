
import customtkinter as ctk
import tkinter as tk
from PIL import Image


def menu():
# Configurasi Window
    from view.input import opencv
    from view.detect import detect_face
    app = ctk.CTk()
    # app.overrideredirect(True)  # Hilangkan title bar (tidak bisa dipindah)
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    app.title("Face Detection")
    app.iconbitmap("icon.ico") 
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}+-10+0")
    # app.bind("<Escape>", lambda e: app.destroy())
    
    # membuat frame dan menaruh gambar dan tulisan didalam
    frame = ctk.CTkFrame(app, width=screen_width, height=screen_height*0.4, fg_color=app._fg_color)
    frame.pack(pady = 80)
    # Menampilkan Gambar ke dalam frame
    image = ctk.CTkImage(Image.open("face-recognition.png"), size=(150, 150))
    label = ctk.CTkLabel(frame, image=image, text="")
    label.pack(side="left", padx=30, pady=20)
    # membuat animasi tulisan mengetik dan menghapus otomatis
    texts = ["Face Recognition", "With DeepFace", "Use ArcFace Model"]
    label_font = ctk.CTkLabel(frame, text="", font=("Tahoma", 90, "bold"))
    label_font.pack(side="left", padx=10, pady=20)
    
    # Daftar teks yang akan dianimasikan
    index = 0     # karakter
    text_index = 0  # teks ke berapa di list
    typing = True  # mode: mengetik atau menghapus
    
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