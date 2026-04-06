class Barang:
  def __init__(self, id_barang, nama):
      self.id_barang = id_barang
      self.nama = nama

class Gudang:
  def __init__(self):
    self.koleksi_barang = []

  def tambah_barang(self, barang_baru):
    self.koleksi_barang.append(barang_baru)
    print(f"{barang_baru.nama} berhasil masuk gudang.")

  def tampilkan_semua(self):
    print("\n---daftar barang di gudang---")
    for item in self.koleksi_barang:
      print(f"ID: {item.id_barang} | Nama: {item.nama}")

  def cari_by_id(self, id_cari):
      for item in self.koleksi_barang:
          if item.id_barang == id_cari:
            return item
      return None

  def filter_nama(self, kata_kuci):
    hasil = [item for item in self.koleksi_barang if kata_kuci.lower() in item.nama.lower()]
    return hasil

  def hitung_total_aset(self):
    total = sum(item.harga for item in self.koleksi_barang)
    return total

  def urutkan_nama(self):
    self.koleksi_barang.sort(key=lambda x: x.nama)
    print("sorting selesai.")

  def tambah_dengan_validasi(self, barang_baru):
    if any(item.id_barang == barang_baru.id_barang for item in self.koleksi_barang):
      print("Eror: id sudah terdaftar")
    else:
      self.koleksi_barang.append(barang_baru)

  def hapus_barang(self, id_hapus):
    objek = self.cari_by_id(id_hapus)
    if objek:
      self.koleksi_barang.remove(objek)
      print(f"barang id {id_hapus} telah dihapus.")
    else:
      print("barang tidak ditemukan")

  def update_nama(self, id_target, nama_baru):
    objek = self.cari_by_id(id_target)
    if objek:
      objek.nama = nama_baru
      print("nama brang berhasil di perbarui")

# inisialisasi sistem
gudang_utama = Gudang()

# create data
gudang_utama.tambah_barang(Barang("A1","Laptop ASUS"))
gudang_utama.tambah_barang(Barang("B2","Mouse Logi"))

# read data
gudang_utama.tampilkan_semua()

# update data
gudang_utama.update_nama("B2","Mouse Logitech Wireless")

# search data
hasil = gudang_utama.cari_by_id("A1")
if hasil:
  print(f"hasil cari: {hasil.nama}")

# delete data
gudang_utama.hapus_barang("A1")
gudang_utama.tampilkan_semua()