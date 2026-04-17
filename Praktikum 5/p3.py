class Barang:
  def __init__(self, id_barang, nama, harga):
    self.id_barang = id_barang
    self.nama = nama
    self.harga = harga

  def info(self):
    return f"[{self.id_barang}] {self.nama:15} | Rp{self.harga:10}"
  
  def to

class BarangElektronik(Barang):
  def __init__(self, id_barang, nama, harga, garansi):
    super().__init__(id_barang, nama, harga)
    self.garansi = garansi
  def info(self):
    return f"{super().info()} | Garansi: {self.garansi} bln"

class BarangKonsumsi(Barang):
  def __init__(self, id_barang, nama, harga, tgl_exp):
    super().__init__(id_barang, nama, harga)
    self.tgl_exp = tgl_exp

  def info(self):
    return f"{super().info()} | Tgl Exp: {self.tgl_exp}"

barang1 = BarangElektronik("B001", "Laptop", 15000000, 24)
barang2 = BarangKonsumsi("B002", "Susu", 50000, "15-12-2026")

print(barang1.info())
print(barang2.info())