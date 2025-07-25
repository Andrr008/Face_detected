import customtkinter as ctk
import tkinter as tk

# Inisialisasi customtkinter
ctk.set_appearance_mode("light")  # atau "dark"
ctk.set_default_color_theme("blue")

# Membuat window utama
root = ctk.CTk()
root.title("Form Input")
root.geometry("300x300")

# Label dan Entry untuk Nama
label_nama = ctk.CTkLabel(root, text="Nama:")
label_nama.pack(pady=(20, 5))

entry_nama = ctk.CTkEntry(root, width=200)
entry_nama.pack()

# Label dan Dropdown untuk Jenis Kelamin
label_gender = ctk.CTkLabel(root, text="Jenis Kelamin:")
label_gender.pack(pady=(15, 5))

# Opsi dropdown dan mapping value
gender_options = {"Laki-laki": "l", "Perempuan": "p"}
gender_dropdown = ctk.CTkOptionMenu(root, values=list(gender_options.keys()))
gender_dropdown.pack()
gender_dropdown.set("Laki-laki")  # set default

# Label untuk pesan validasi
label_error = ctk.CTkLabel(root, text="", text_color="red")
label_error.pack(pady=5)

# Fungsi saat submit
def submit():
    nama = entry_nama.get().strip()
    if not nama:
        label_error.configure(text="Nama harus diisi!")
    else:
        gender_label = gender_dropdown.get()
        gender_value = gender_options[gender_label]
        print(f"Nama: {nama}")
        print(f"Jenis Kelamin: {gender_label} (value = {gender_value})")

        # Reset form
        entry_nama.delete(0, tk.END)
        gender_dropdown.set("Laki-laki")
        label_error.configure(text="")
        root.destroy()

# Tombol Submit
submit_button = ctk.CTkButton(root, text="Submit", command=submit)
submit_button.pack(pady=20)

root.mainloop()
