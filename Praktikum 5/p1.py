class Karyawan:
    def __init__ (self,nama):
        self.nama = nama
        
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__ (self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan
        
class K