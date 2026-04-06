def to_dict(self):
  """Mengonversi objek ke dictionary agar bisa disimpan ke JSON"""
  return {"id": self.id_barang, "nama": self.nama, "harga": self.harga}

def __init__(self, file_db='database_gudang.json'):
  self.file_db = file_db
  self.koleksi_barang = []
  self.muat_data()

def simpan_data(self):
  """Menyimpan data ke dalam file JSON"""
  try:
    with open(self.file_db, 'w') as f:
      data_json = [item.to_dict() for item in self.koleksi_barang]
      json.dump(data_json, f, indent=4)
  except Exception as e:
    print(f"Gagal menyimpan data: {e}")

def muat_data(self):
  """Memuat data dari JSON dan mengubah nya kembali menjadi objek barang"""
  if os.path.exists(self.file_db):
    try:
      with open(self.file_db, 'r') as f:
        data_load = json.load(f)
        self.koleksi_barang = [Barang(d['id'], d['nama'], d['harga']) for d in data_load]
    except Exception as e:
      print(f"Gagal memuat data lama: {e}")

def tambah_barang(self, barang_baru):
    if any(item.id_barang == barang_baru.id_barang for item in self.koleksi_barang):
      return False, "ID sudah terdaftar!"
    self.koleksi_barang.append(barang_baru)
    self.simpan_data()
    return True, "Berhasil di tambahkan"

def hapus_barang(self, id_hapus):
    for item in self.koleksi_barang:
      if item.id_barang == id_hapus:
        self.koleksi_barang.remove(item)
        self.simpan_data()
        return True
    return False

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