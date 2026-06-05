import tkinter as tk
from tkinter import messagebox
import json
import os
main.py = "users.json"

# Fungsi untuk memuat data pengguna
def load_users():
 if not os.path.exists(FILE_NAME):
 return {}
 with open(FILE_NAME, "r") as f:
 return json.load(f)
 
# Fungsi untuk menyimpan data pengguna
def save_users(users):
 with open(FILE_NAME, "w") as f:
 json.dump(users, f)

def register():
 user = entry_user.get()
 pwd = entry_pwd.get()
 users = load_users()
 if user in users:
 messagebox.showerror("Error", "Username sudah
terdaftar!")
 else:
 users[user] = pwd
 save_users(users)
 messagebox.showinfo("Success", "Registrasi Berhasil!")
 
 # Logic Login
def login():
 user = entry_user.get()
 pwd = entry_pwd.get()
 users = load_users()
 if users.get(user) == pwd:
 messagebox.showinfo("Login", "Login Berhasil! Selamat
Datang.")
 else:
     messagebox.showerror("Login", "Username atau Password
Salah!")