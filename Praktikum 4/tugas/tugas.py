# DATASET
produk_marketplace = [
    {"nama": "Laptop Gaming", "harga": 15000000, "kategori": "Elektronik", "garansi": 24, "stok": 5},
    {"nama": "Kemeja Flanel", "harga": 200000, "kategori": "Pakaian", "ukuran": "M", "stok": 10},
    {"nama": "Smart TV", "harga": 7000000, "kategori": "Elektronik", "garansi": 12, "stok": 3},
    {"nama": "Celana Jeans", "harga": 300000, "kategori": "Pakaian", "ukuran": "L", "stok": 7}
]

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info(self):
        return f"{self.nama:15} | Rp{self.harga:10} | Stok: {self.stok}"

class Elektronik(Produk):
    def __init__(self, nama, harga, stok, garansi):
        super().__init__(nama, harga, stok)
        self.garansi = garansi

    def info(self):
        return f"{super().info()} | Garansi: {self.garansi} bln"

class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran

    def info(self):
        return f"{super().info()}  | Ukuran: {self.ukuran}"

produk_list = []

for item in produk_marketplace:
    if item["kategori"] == "Elektronik":
        produk = Elektronik(
            item["nama"],
            item["harga"],
            item["garansi"],
            item["stok"]
        )
    else:
        produk = Pakaian(
            item["nama"],
            item["harga"],
            item["ukuran"],
            item["stok"]
        )
    produk_list.append(produk)


def hitung_total(keranjang):
    return sum(item.harga for item in keranjang)

keranjang = [
    produk_list[0],  # Laptop Gaming
    produk_list[1],  # Kemeja Flanel
    produk_list[2]   # Smart TV
]

print("=== DAFTAR BELANJA ===")
for item in keranjang:
    print(item.info())

total = hitung_total(keranjang)

print("\nTOTAL BELANJA:")
print(f"Rp{total}")