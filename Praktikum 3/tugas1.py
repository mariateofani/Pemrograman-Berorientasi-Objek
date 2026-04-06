class Karyawan:
    def __init__(self, nik, nama, jabatan):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan


class SistemKaryawan:
    def __init__(self):
        self.database = []

    def tambah_karyawan(self, karyawan):
        # cek NIK duplikat
        for k in self.database:
            if k.nik == karyawan.nik:
                print("❌ NIK sudah ada! Tidak boleh duplikat.")
                return
        self.database.append(karyawan)
        print("✅ Karyawan berhasil ditambahkan!")

    def cari_karyawan(self, nik):
        for k in self.database:
            if k.nik == nik:
                print("\nData Karyawan Ditemukan:")
                print(f"NIK     : {k.nik}")
                print(f"Nama    : {k.nama}")
                print(f"Jabatan : {k.jabatan}")
                return
        print("❌ Karyawan tidak ditemukan.")

    def tampilkan_semua(self):
        if not self.database:
            print("📭 Data karyawan kosong.")
            return

        print("\n=== DAFTAR KARYAWAN ===")
        print("{:<10} {:<15} {:<15}".format("NIK", "Nama", "Jabatan"))
        print("-" * 40)
        for k in self.database:
            print("{:<10} {:<15} {:<15}".format(k.nik, k.nama, k.jabatan))


# Program Utama
def main():
    sistem = SistemKaryawan()

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Karyawan")
        print("2. Cari Karyawan (NIK)")
        print("3. Lihat Semua")
        print("4. Keluar")

        pilihan = input("Pilihan: ")

        if pilihan == "1":
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            jabatan = input("Masukkan Jabatan: ")

            karyawan = Karyawan(nik, nama, jabatan)
            sistem.tambah_karyawan(karyawan)

        elif pilihan == "2":
            nik = input("Masukkan NIK yang dicari: ")
            sistem.cari_karyawan(nik)

        elif pilihan == "3":
            sistem.tampilkan_semua()

        elif pilihan == "4":
            print("👋 Program selesai.")
            break

        else:
            print("❌ Pilihan tidak valid!")


# Jalankan program
if __name__ == "__main__":
    main()
