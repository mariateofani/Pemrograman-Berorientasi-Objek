# PHYTON LIST 

# Mendefinisikan list daya sistem (Sistem Monitoring Kesehatan Sederhana)
detak_jantung = [70, 110, 65, 120, 80, 140]

#Mengakses data berdasarkan index (dimulai dari 0)
print(f"Data Pertama : {detak_jantung[0]} bpm\n")


# Menambah data baru
detak_jantung.append(75)


#FUNCTION

#Fungsi untuk menganalisa kondisi detak jantung
def analisa_kondisi(bpm):
    if bpm > 100:
        return "Peringatan Takikardia (Detak Tinggi)"
    else:
        return "Kondisi Normal"
        
        
# ITERATION
# Mencetak semua data detak jantung
print("Daftar Riwayat Detak Jantung:")

for data in detak_jantung:
    print(f"Data ke-[x]: {data} BPM")
    
    
    