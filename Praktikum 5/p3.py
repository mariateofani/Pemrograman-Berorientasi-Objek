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
       self file_db = file_db
       self koleksi = []
       self muat_data()

   def tambah_barang(self, objek_barang):
       self.koleksi.append(objek_barang)
       self.simpan_data()
       
    def simpan_data(self):
        with open (sefl.file_db, 'w') as f:
            data = b.to_dict() for b in self.koleksi]
            json.dump(data, f, indent=4)
            
           
def muat_data(self):
    if os.path.exists(self.file_db):
        with open(self.file db, 'r') as f: 
        data_list = json.load(f)
        self.koleksi []
        for d in data_list:
            
            if d['tipe'] == "elektronik" :
                obj = BarangElektronik(d['id'], d['nama'], d['harga'), di garansi'])
            elif d['tipe'] == "konsumsi":
                obj Barangkonsumsi (d['id'], d['nama'], d['harga'], d['tgl_exp'])
            else:
                obj = Barang(d['id'], d['nama'], d['harga'])
            self.koleksi.append(obj)

def laporan stok(self):
    print("\n"+""*70)
    print(f"("ID":6} | NAMA BARANG:18) | ('HARGA:13) | KETERANGAN TAMBAHAN")")
    print(70)
    for bin self.koleksi:

        print(b.info())
    print("**70)
 
barang1 = BarangElektronik("B001", "Laptop", 15000000, 24)
barang2 = BarangKonsumsi("B002", "Susu", 50000, "15-12-2026")

print(barang1.info())
print(barang2.info())