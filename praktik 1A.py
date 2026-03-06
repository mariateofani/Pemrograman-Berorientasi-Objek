# PHYTON LIST 

# Mendefinisikan list daya sistem (Sistem Monitoring Kesehatan Sederhana)
detak_jantung = [81.6, 80.2, 78.5, 75.3, 73.9]

#Mengakses data berdasarkan index (dimulai dari 0)
print(f"Data Pertama : {detak_jantung[0]} bpm\n")


# Menambah data baru
detak_jantung.append(72.8)


# ITERATION

# Mencetak semua data detak detak_jantung
print("Daftar rentan detak jantung saat istirahat : \n")
for data in detak_jantung :
    print(f"Detak jantung: {data} bpm")
    

#FUNCTION

#Fungsi untuk mengecek detak jantung berdasarkan usia
def cek(index):
    if index == 0:
        return "18-20 tahun"
    elif index == 1:
        return "21-30 tahun"
    elif index == 2:
        return "31-40 tahun"
    elif index == 3:
        return "41-50 tahun"
    elif index == 4:
        return "51-60 tahun"
    else:
        return "60+ tahun"
        
        
for data in detak_jantung:
    usia = cek(data)
    print(f"Detak Jantung {data} -> usia: {usia} ")