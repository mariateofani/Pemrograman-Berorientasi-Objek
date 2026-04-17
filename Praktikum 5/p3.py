import json
from datetime import datetime

class Barang:
    def __init__(self, id_barang, nama, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"[{self.id_barang}] {self.nama:15} | Rp{self.harga:10}"

    def to_dict(self):
        return {
            "id_barang": self.id_barang,
            "nama": self.nama,
            "harga": self.harga,
            "tipe": "umum"
        }


class BarangElektronik(Barang):
    def __init__(self, id_barang, nama, harga, garansi):
        super().__init__(id_barang, nama, harga)
        self.garansi = garansi

    def info(self):
        return f"{super().info()} | Garansi: {self.garansi} bln"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "garansi": self.garansi,
            "tipe": "elektronik"
        })
        return data


class BarangKonsumsi(Barang):
    def __init__(self, id_barang, nama, harga, tgl_exp):
        super().__init__(id_barang, nama, harga)
        self.tgl_exp = tgl_exp

    def info(self):
        # ✅ Tugas Mandiri: Cek kadaluarsa
        today = datetime.now().strftime("%d-%m-%Y")

        if self.tgl_exp < today:
            status = " (EXPIRED!)"
        else:
            status = ""

        return f"{super().info()} | Tgl Exp: {self.tgl_exp}{status}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tgl_exp": self.tgl_exp,
            "tipe": "konsumsi"
        })
        return data