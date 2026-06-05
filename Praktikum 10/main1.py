import json
import os

FILE_NAME = "users.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

def register():
    user = input("Masukkan Username: ")
    pwd = input("Masukkan Password: ")

    if user == "" or pwd == "":
        print("Error: Username dan Password tidak boleh kosong!")
        return

    users = load_users()
    if user in users:
        print("Error: Username sudah terdaftar!")
    else:
        users[user] = pwd
        save_users(users)
        print("Registrasi Berhasil!")

def login():
    user = input("Masukkan Username: ")
    pwd = input("Masukkan Password: ")

    if user == "" or pwd == "":
        print("Error: Username dan Password tidak boleh kosong!")
        return

    users = load_users()
    if users.get(user) == pwd:
        print("Login Berhasil! Selamat Datang,", user)
    else:
        print("Login Gagal: Username atau Password Salah!")

# Menu utama
while True:
    print("\n=== MENU LOGIN/REGISTER ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        login()
    elif pilihan == "2":
        register()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid!")