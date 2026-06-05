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
