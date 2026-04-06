class Barang:
  def __init__(self, id_barang, nama, harga):
      self.id_barang = id_barang
      self.nama = nama
      self.harga = harga

  def __str__(self):
      return f"| {self.id_barang:8} | {self.nama:20} | Rp{self.harga:10,} |"

class Gudang:
  def __init__(self):
    self.koleksi_barang = []

  def tambah_barang(self, barang_baru):
      if any(item.id_barang == barang_baru.id_barang for item in self.koleksi_barang):
        return False, "ID sudah terdaftar!"
      self.koleksi_barang.append(barang_baru)
      return True, "Berhas ditambahkan."

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


  def tampilkan_semua(self):
      if not self.koleksi_barang:
        print("\n [Gudang Kosong]")
        return
      print("\n" + "="*50)
      print(f"| {'ID':8} | {'NAMA BARANG':20} | {'HARGA':10} |")
      print("-" * 50)
      for item in self.koleksi_barang:
        print(item)
      print("=" * 50)

def main():
    app = Gudang()
    print("Variabel 'app' sudah terdaftar di memori Colab!")

    while True:
      print("\n>>> SISTEM MANAJEMEN GUDANG V.1.0 <<<")
      print("1. Tambah Barang Baru")
      print("2. Lihat Semua Inventaris")
      print("3. Cari Barang (ID)")
      print("4. Hapus Barang")
      print("5. keluar")

      pilihan = input("pilih Menu (1-5): ")
      if pilihan == "1":
        print("\n--- Input Barang Baru ---")
        id_b = input("Masukan ID Barang: ")
        nama = input("Masukan Nama Barang: ")
        try:
          harga = int(input("Masukan Harga: "))
          status, pesan = app.tambah_barang(Barang(id_b, nama, harga))
          print(f"Status: {pesan}")
        except ValueError:
          print("Input Gagal: Harga harus berupa angka.")

      elif pilihan == "2":
        app.tampilkan_semua()

      elif pilihan == "3":
        id_c = input("\nMasukan ID yang dicari: ")
        hasil = app.cari_by_id(id_c)
        if hasil:
          print(f" Ditemukan: {hasil.nama} - Rp{hasil.harga:,}")
        else:
          print("Barang tidak ditemukan.")

      elif pilihan == "4":
        id_h = input("\nMasukan ID yang akan dihapus: ")
        if app.hapus_barang(id_h):
          print("Barang berhasil dihapus dari sistem.")
        else:
          print("Gagal: ID tidak ditemukan.")

      elif pilihan == "5":
        print("Terima kasih program selesai.")
        break

      else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")

if __name__ == "__main__":
    main()