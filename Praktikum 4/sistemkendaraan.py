class Kendaraan:
  def __init__(self, id_kendaraan, merk, kecepatan):
    self.id_kendaraan = id_kendaraan
    self.merk = merk
    self.kecepatan = kecepatan

  def info(self):
    print(f"ID: {self.id_kendaraan}, Merk: {self.merk}, Kecepatan: {self.kecepatan}")

class Mobil(Kendaraan):
  def __init__(self, id_kendaraan, merk, kecepatan, jumlah_pintu):
    super().__init__(id_kendaraan, merk, kecepatan)
    self.jumlah_pintu = jumlah_pintu

  def info(self):
    super().info()
    print(f"Jumlah pintu: {self.jumlah_pintu}")

class Motor(Kendaraan):
  def __init__(self, id_kendaraan, merk, kecepatan, jenis):
    super().__init__(id_kendaraan, merk, kecepatan)
    self.jenis = jenis

  def info(self):
    super().info()
    print(f"Jenis: {self.jenis}")

mobil1 = Mobil("M001", "Toyota", 120, 4)
motor1 = Motor("M002", "Honda", 100, "Sport")

print(mobil1.info())
print(motor1.info())