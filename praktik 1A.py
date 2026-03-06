# PHYTON LIST 

# Mendefinisikan list daya sistem (Sistem Monitoring Kesehatan Sederhana)
detak_jantung = [81.6, 80.2, 78.5, 75.3, 73.9]

#Mengakses data berdasarkan index (dimulai dari 0)
print(f"usia 18-20 tahun : {detak_jantung[0]} bpm")
print(f"usia 21-30 tahun : {detak_jantung[1]} bpm")
print(f"usia 31-40 tahun : {detak_jantung[2]} bpm")
print(f"usia 41-50 tahun : {detak_jantung[3]} bpm")
print(f"usia 51-60 tahun : {detak_jantung[4]} bpm")

# Menambah data baru
detak_jantung.append(72.8)

print(f"usia < 60 tahun : {detak_jantung[5]} bpm")


# ITERATION

# Mencetak semua data detak detak_jantung
print("Daftar rentan detak jantung saat istirahat : ")
for data in detak_jantung :
    print(f"Detak jantung: {data} bpm")
    

#FUNCTION

#Fungsi untuk mengecek detak jantung berdasarkan usia
def cek(data):
    if data >= 81 and umur <= 82:
        return("Usia 18-20 tahun")
    elif data >= 79 and umur <= 81:
        return("Usia 21-30 tahun")
    elif data >= 76 and umur <= 79:
        return("Usia 31-40 tahun")
    elif data >= 78 and umur <= 76:
        return("Usia 41-50 tahun")
    elif data >=
        return("Usia 51-60 tahun")
    else:
        return("Usia 60 keatas / Lansia")
    
for data in detak_jantung:
    usia = cek(data)
    print(f"Detak Jantung {data} -> usia: {usia} ")