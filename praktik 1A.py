# PHYTON LIST 

# Mendefinisikan list daya sistem (Sistem Monitoring Kesehatan Sederhana)
detak_jantung = [70, 110, 65, 120, 80, 140]

#Mengakses data berdasarkan index (dimulai dari 0)
print(f"Data Pertama : {detak_jantung[0]} bpm\n")


# Menambah data baru
detak_jantung.append(75)


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
        return "18-20 tahun"
    elif data == 80.2:
        return "21-30 tahun"
    elif data == 78.5:
        return "31-40 tahun"
    elif data == 75.3:
        return "41-50 tahun"
    elif data == 73.9:
        return "51-60 tahun"
    else:
        return "60 tahun ke atas"
        
for data in detak_jantung:
    usia = cek(data)
    print(f"Detak Jantung {data} bpm -> Usia: {usia} ")
    
    
    
    