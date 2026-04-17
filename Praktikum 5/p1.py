def tambah (a, b):
    return a + b
    
    print(tambah(2, 3))
    print(tambah("Hello", "AI"))
   
    print("/n")
   
   
def kali (c, d):
    return c * d
    
    print(kali(2,3))
    print(kali("Hello", 3))

class Kendaraan:
    def berjalan(self):
        print("Kendaraan sedang berjalan")
  
class Pesawat(Kendaraan):
    def berjalan(self):
        print("Pesawat terbang di udara")
        
class Mobil(Kendaraan):
    def berjalan(self):
        print("Mobil berjalan di jalan raya")
        
class Motor(Kendaraan):
    def berjalan(self):
        print("Motor berjalan di jalan raya")
        
daftar_kendaraan