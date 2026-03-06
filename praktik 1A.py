# PHYTON LIST 

# Mendefinisikan list daya sistem (Sistem Monitoring Kesehatan Sederhana)
detak_jantung = [81.6, 80.2, 78.5, 75.3, 73.9]

#Mengakses data berdasarkan index (dimulai dari 0)
print(f"Data Pertama : {detak_jantung[0]} bpm\n")


# Menambah data baru
detak_jantung.append(72.8)


# ITERATION

# Mencetak semua data detak detak_jantung
print("Daftar rentan detak jantung saat istirahat : ")
for data in detak_jantung :
    print(f"Detak jantung: {data} bpm")
 print()
    

#FUNCTION

#Fungsi untuk mengecek detak jantung berdasarkan usia
print("Data detak jantung normal : ")
def cek(data):
    if data == 81.6:
        return "Usia 18-20 tahun"
    elif data == 80.2:
        return "Usia 21-30 tahun"
    elif data == 78.5:
        return "Usia 31-40 tahun"
    elif data == 75.3:
        return "Usia 41-50 tahun"
    elif data == 73.9:
        return "Usia 51-60 tahun"
    else:
        return "Usia 60 tahun ke atas"

        
for data in detak_jantung:
    usia = cek(data)
    print(f"Detak Jantung {data} -> usia: {usia} ")