class Hewan:
    def __init__(self, nama_hewan, jenis):
        self.nama_hewan = nama_hewan
        self.jenis = jenis

    def tampilkan_info(self):
        print(f"Nama Hewan: {self.nama_hewan}")
        print(f"Jenis: {self.jenis}")

class Kucing(Hewan):
    def __init__(self, nama_hewan, jenis, warna, jenis_bulu):
        super().__init__(nama_hewan, jenis)
        self.warna = warna
        self.jenis_bulu = jenis_bulu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Warna: {self.warna}")
        print(f"Jenis Bulu: {self.jenis_bulu}")
        print()


class Paus(Hewan):
    def __init__(self, nama_hewan, jenis, ukuran, berat):
        super().__init__(nama_hewan, jenis)
        self.ukuran = ukuran
        self.berat = berat

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Ukuran: {self.ukuran}")
        print(f"Berat: {self.berat}")
        print()

class Singa(Hewan):
    def __init__(self, nama_hewan, jenis, berat, asal):
        super().__init__(nama_hewan, jenis)
        self.berat = berat
        self.asal = asal

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Berat: {self.berat}")
        print(f"Asal: {self.asal}")
        print()

kucing1 = Kucing("Kucing", "Mamalia", "Putih", "Panjang")
paus1 = Paus("Paus", "Mamalia", "30 meter", "120 ton")
singa1 = Singa("Singa", "Mamalia", "190 kg", "Afrika")

kucing1.tampilkan_info()
paus1.tampilkan_info()
singa1.tampilkan_info()