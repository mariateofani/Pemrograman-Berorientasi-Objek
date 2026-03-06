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
    print(f"- Nilai")