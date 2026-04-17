class Karyawan:
    def __init__(self,nama):
        self.nama = nama
        
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__ (self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan
        
class KaryawanFreelance(Karyawan):
    def __init__(self, nama,jam_kerja,tarif_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam
        
    def hitung_gaji(self):
        return self.jam_kerja * tarif_per_jam
        
daftar_karyawan = [
    Karyawan]