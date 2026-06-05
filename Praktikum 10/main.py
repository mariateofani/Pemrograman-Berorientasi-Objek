
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "users.json" # nama file buat nyimpen data user

# Fungsi untuk memuat data pengguna
def load_users():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Fungsi untuk menyimpan data pengguna
def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4) # indent=4 biar file json nya rapi

# Fungsi Register
def register():
    user = entry_user.get()
    pwd = entry_pwd.get()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "Username dan Password tidak boleh kosong!")
        return

    users = load_users()

    if user in users:
        messagebox.showerror("Error", "Username sudah terdaftar!")
    else:
        users[user] = pwd
        save_users(users)
        messagebox.showinfo("Success", "Registrasi Berhasil!")
        entry_user.delete(0, tk.END)
        entry_pwd.delete(0, tk.END)

# Fungsi Login
def login():
    user = entry_user.get()
    pwd = entry_pwd.get()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "Username dan Password tidak boleh kosong!")
        return

    users = load_users()

    if users.get(user) == pwd:
        messagebox.showinfo("Login", "Login Berhasil! Selamat Datang.")
        entry_user.delete(0, tk.END)
        entry_pwd.delete(0, tk.END)
    else:
        messagebox.showerror("Login", "Username atau Password Salah!")

# Setup UI
root = tk.Tk()
root.title("Sistem Informasi - Login/Register")
root.geometry("300x250")

tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack(pady=5)
# Parameter show="*" digunakan untuk menyamarkan ketikan password
entry_pwd = tk.Entry(root, show="*")
entry_pwd.pack()

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=5)

btn_reg = tk.Button(root, text="Register", command=register)
btn_reg.pack(pady=5)

# Menjalankan perulangan utama agar jendela aplikasi tetap terbuka
root.mainloop()







