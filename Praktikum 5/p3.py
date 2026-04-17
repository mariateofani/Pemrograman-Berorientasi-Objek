import json
import os

class Barang:
  def __init__(self, id_barang, nama, harga):
    self.id_barang = id_barang
    self.nama = nama
    self.harga = harga

  def info(self):
    return f"[{self.id_barang}] {self.nama:15} | Rp{self.harga:10}"
  
  def to_dict(self):
      return {"tipe" : "umum", "id" : self.id_barang,"nama" : self.nama,"harga" : self.harga}

class BarangElektronik(Barang):
  def __init__(self, id_barang, nama, harga, garansi):
    super().__init__(id_barang, nama, harga)
    self.garansi = garansi
  def info(self):
    return f"{super().info()} | Garansi: {self.garansi} bln"
    
  def to_dict(self):
      d = super().to_dict()
      d.update({"tipe" : "elektronik", "garansi" :self.garansi})
      return d

class BarangKonsumsi(Barang):
  def __init__(self, id_barang, nama, harga, tgl_exp):
    super().__init__(id_barang, nama, harga)
    self.tgl_exp = tgl_exp

  def info(self):
    return f"{super().info()} | Tgl Exp: {self.tgl_exp}"
    
    d.update({"tipe" : "konsumsi", "tgl_exp" :self.tgl_exp})
      return d
      
class GudangPolimorfik:
   def __init__(self,file_db= 'gudang_v3.json'):
    super().__init__(id_barang, nama, harga)
    self.tgl_exp = tgl_exp

   def 
    d.update({"tipe" : "konsumsi", "tgl_exp" :self.tgl_exp})
      return 

barang1 = BarangElektronik("B001", "Laptop", 15000000, 24)
barang2 = BarangKonsumsi("B002", "Susu", 50000, "15-12-2026")

print(barang1.info())
print(barang2.info())