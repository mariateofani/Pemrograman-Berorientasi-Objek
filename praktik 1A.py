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
print("Hasil Analisa Detak Jantung:\n")

for data in detak_jantung:
    status = analisa_kondisi(bpm)
    print(f"Data ke-{data}: {bpm} BPM -> {status}")
    
    
    
    