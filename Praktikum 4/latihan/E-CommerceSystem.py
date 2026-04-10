class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama:15} | Rp{self.harga:10}"


class Elektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi

    def diskon(self):
        return self.harga * 0.9  # 10%

    def info(self):
        return f"{super().info()} | Diskon: 10% | Rp{self.diskon():10}"


class Pakaian(Produk):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

    def diskon(self):
        return self.harga * 0.8  # 20%

    def info(self):
        return f"{super().info()} | Diskon: 20% | Rp{self.diskon():10}"

p1 = Elektronik("Laptop", 10000000, "2 Tahun")
p2 = Pakaian("Kaos", 100000, "L")

print(p1.info())
print(p2.info())