class Person:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def tampilkan_info(self):
    print(f"Nama: {self.nama}, Umur: {self.umur}")

class Mahasiswa(Person):
  def __init__(self, nama, umur, nim, jurusan):
    super().__init__(nama, umur)
    self.nim = nim
    self.jurusan = jurusan

  def tampilkan_mahasiswa(self):
    self.tampilkan_info()
    print(f"NIM: {self.nim}, Jurusan: {self.jurusan}")

class Dosen(Person):
  def __init__(self, nama, umur, nip, mata_kuliah):
    super().__init__(nama, umur)
    self.nip = nip
    self.mata_kuliah = mata_kuliah

  def tampilkan_dosen(self):
    self.tampilkan_info()
    print(f"NIP: {self.nip}, Mata Kuliah: {self.mata_kuliah}")

mhs = Mahasiswa("Fadil", 20, "V3925001", "Teknik Informatika")
mhs.tampilkan_mahasiswa()

dsn = Dosen("Dr. Budi", 30, "123456789", "Pemrograman Berorientasi Objek")
dsn.tampilkan_dosen()