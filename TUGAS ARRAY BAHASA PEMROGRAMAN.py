def input_data_mahasiswa():
    mahasiswa_list = []
    n = int(input("MASUKKAN JUMLAH MAHASISWA: "))

    for i in range(n):
        nama = input(f"MASUKKAN NAMA MAHASISWA {i+1}: ")
        nim = input(f"MASUKKAN NIM MAHASISWA {i+1}: ")
        jurusan = input(f"MASUKKAN PRODI MAHASISWA {i+1}: ")
        nilai = float(input(f"MASUKKAN NILAI MAHASISWA {i+1}: "))

        mahasiswa = (nama, nim, jurusan, nilai)
        mahasiswa_list.append(mahasiswa)

    return mahasiswa_list

def tampilkan_data_mahasiswa(mahasiswa_list):
    print("\nDATA MAHASISWA:")
    for mahasiswa in mahasiswa_list:
        print(f"NAMA: {mahasiswa[0]}, NIM: {mahasiswa[1]}, PRODI: {mahasiswa[2]}, NILAI: {mahasiswa[3]}")

def hitung_rata_rata(mahasiswa_list):
    total_nilai = sum(mahasiswa[3] for mahasiswa in mahasiswa_list)
    rata_rata = total_nilai / len(mahasiswa_list)
    print(f"\nRATA-RATA NILAI MAHASISWA: {rata_rata:.2f}")

def cari_nilai_tertinggi_terendah(mahasiswa_list):
    nilai_tertinggi = mahasiswa_list[0]
    nilai_terendah = mahasiswa_list[0]

    for mahasiswa in mahasiswa_list:
        if mahasiswa[3] > nilai_tertinggi[3]:
            nilai_tertinggi = mahasiswa
        if mahasiswa[3] < nilai_terendah[3]:
            nilai_terendah = mahasiswa

    print(f"\nMAHASISWA DENGAN NILAI TERTINGGI ADALAH : {nilai_tertinggi[0]} - DENGAN NILAI: {nilai_tertinggi[3]}")
    print(f"MAHASISWA DENGAN NILAI TERENDAH ADALAH: {nilai_terendah[0]} - DENGAN NILAI: {nilai_terendah[3]}")

def input_data_barang():
    barang_list = []
    n = int(input("MASUKKAN JUMLAH BARANG: "))

    for i in range(n):
        nama = input(f"MASUKKAN NAMA BARANG {i+1}: ")
        kode = input(f"MASUKKAN KODE BARANG {i+1}: ")
        jumlah = int(input(f"MASUKKAN JUMLAH BARANG {i+1}: "))

        barang = (nama, kode, jumlah)
        barang_list.append(barang)

    return barang_list

def tampilkan_data_barang(barang_list):
    print("\nDATA BARANG:")
    for barang in barang_list:
        print(f"NAMA: {barang[0]}, KODE: {barang[1]}, JUMLAH: {barang[2]}")

def cari_barang_berdasarkan_kode(barang_list, kode):
    for barang in barang_list:
        if barang[1] == kode:
            return barang
    return None

def tambah_barang(barang_list):
    nama = input("MASUKKAN NAMA BARANG: ")
    kode = input("MASUKKAN KODE BARANG: ")
    jumlah = int(input("MASUKKAN JUMLAH BARANG: "))
    barang = (nama, kode, jumlah)
    barang_list.append(barang)

def hapus_barang(barang_list):
    kode = input("MASUKKAN KODE BARANG YANG INGIN DIHAPUS: ")
    for barang in barang_list:
        if barang[1] == kode:
            barang_list.remove(barang)
            print("BARANG BERHASIL DIHAPUS.")
            return
    print("BARANG TIDAK DITEMUKAN.")

class Warung:
    def __init__(self):
        self.transaksi_penjualan = []
        self.transaksi_pembelian = []

    def tambah_transaksi_penjualan(self, nama_barang, harga_jual):
        self.transaksi_penjualan.append((nama_barang, harga_jual))

    def tambah_transaksi_pembelian(self, nama_barang, harga_beli):
        self.transaksi_pembelian.append((nama_barang, harga_beli))

    def tampilkan_transaksi_penjualan(self):
        if not self.transaksi_penjualan:
            print("BELUM ADA TRANSAKSI PENJUALAN YANG DITAMBAHKAN.")
        else:
            print("DAFTAR TRANSAKSI PENJUALAN:")
            for idx, transaksi in enumerate(self.transaksi_penjualan, start=1):
                print(f"TRANSAKSI {idx}: NAMA BARANG: {transaksi[0]}, HARGA JUAL: {transaksi[1]}")

    def tampilkan_transaksi_pembelian(self):
        if not self.transaksi_pembelian:
            print("BELUM ADA TRANSAKSI PEMBELIAN YANG DITAMBAHKAN.")
        else:
            print("DAFTAR TRANSAKSI PEMBELIAN:")
            for idx, transaksi in enumerate(self.transaksi_pembelian, start=1):
                print(f"TRANSAKSI {idx}: NAMA BARANG: {transaksi[0]}, HARGA BELI: {transaksi[1]}")

    def total_penjualan(self):
        return sum(transaksi[1] for transaksi in self.transaksi_penjualan)

    def total_pembelian(self):
        return sum(transaksi[1] for transaksi in self.transaksi_pembelian)

    def laba_bersih(self):
        return self.total_penjualan() - self.total_pembelian()

    def tampilkan_saldo(self):
        saldo = self.total_penjualan() - self.total_pembelian()
        print(f"SALDO WARUNG: {saldo}")

    def input_transaksi(self, jenis_transaksi):
        nama_barang = input("MASUKKAN NAMA BARANG: ")
        harga = float(input(f"MASUKKAN HARGA {jenis_transaksi} BARANG: "))
        if jenis_transaksi == "JUAL":
            self.tambah_transaksi_penjualan(nama_barang, harga)
        elif jenis_transaksi == "BELI":
            self.tambah_transaksi_pembelian(nama_barang, harga)
        print(f"TRANSAKSI {jenis_transaksi} BERHASIL DITAMBAHKAN!")

    def tampilkan_semua_transaksi(self):
        self.tampilkan_transaksi_penjualan()
        self.tampilkan_transaksi_pembelian()

    def total_pemasukan(self):
        return self.total_penjualan()

    def total_pengeluaran(self):
        return self.total_pembelian()

    def saldo_akhir(self):
        return self.laba_bersih()

# Fungsi utama
def main():
    mahasiswa_list = []
    barang_list = []
    warung = Warung()

    while True:
        print("\nMENU UTAMA:")
        print("1. KELOLA DATA MAHASISWA")
        print("2. KELOLA DATA BARANG")
        print("3. KELOLA DATA WARUNG")
        print("4. KELUAR")

        pilihan = input("PILIH MENU: ")

        if pilihan == '1':
            while True:
                print("\nMENU MAHASISWA:")
                print("1. MASUKKAN DATA MAHASISWA")
                print("2. TAMPILKAN DATA MAHASISWA")
                print("3. HITUNG RATA-RATA NILAI MAHASISWA")
                print("4. CARI NILAI TERTINGGI DAN TERENDAH")
                print("5. KEMBALI KE MENU UTAMA")

                pilihan_mahasiswa = input("PILIH MENU: ")

                if pilihan_mahasiswa == '1':
                    mahasiswa_list = input_data_mahasiswa()
                elif pilihan_mahasiswa == '2':
                    tampilkan_data_mahasiswa(mahasiswa_list)
                elif pilihan_mahasiswa == '3':
                    hitung_rata_rata(mahasiswa_list)
                elif pilihan_mahasiswa == '4':
                    cari_nilai_tertinggi_terendah(mahasiswa_list)
                elif pilihan_mahasiswa == '5':
                    break
                else:
                    print("PILIHAN TIDAK VALID, SILAHKAN PILIH MENU YANG SESUAI.")

        elif pilihan == '2':
            while True:
                print("\nMENU BARANG:")
                print("1. MASUKKAN DATA BARANG")
                print("2. TAMPILKAN DATA BARANG")
                print("3. CARI BARANG BERDASARKAN KODE")
                print("4. TAMBAH BARANG")
                print("5. HAPUS BARANG")
                print("6. KEMBALI KE MENU UTAMA")

                pilihan_barang = input("PILIH MENU: ")

                if pilihan_barang == '1':
                    barang_list = input_data_barang()
                elif pilihan_barang == '2':
                    tampilkan_data_barang(barang_list)
                elif pilihan_barang == '3':
                    kode_cari = input("MASUKKAN KODE BARANG YANG INGIN DICARI: ")
                    barang_ditemukan = cari_barang_berdasarkan_kode(barang_list, kode_cari)
                    if barang_ditemukan:
                        print(f"BARANG DITEMUKAN: NAMA: {barang_ditemukan[0]}, KODE: {barang_ditemukan[1]}, JUMLAH: {barang_ditemukan[2]}")
                    else:
                        print("BARANG DENGAN KODE TERSEBUT TIDAK DITEMUKAN.")
                elif pilihan_barang == '4':
                    tambah_barang(barang_list)
                elif pilihan_barang == '5':
                    hapus_barang(barang_list)
                elif pilihan_barang == '6':
                    break
                else:
                    print("PILIHAN TIDAK VALID, SILAHKAN PILIH MENU YANG SESUAI.")

        elif pilihan == '3':
            while True:
                print("\nMENU WARUNG:")
                print("1. TAMBAHKAN TRANSAKSI PENJUALAN")
                print("2. TAMBAHKAN TRANSAKSI PEMBELIAN")
                print("3. TAMPILKAN SEMUA TRANSAKSI")
                print("4. TOTAL PEMASUKAN")
                print("5. TOTAL PENGELUARAN")
                print("6. SALDO AKHIR")
                print("7. KEMBALI KE MENU UTAMA")

                pilihan_warung = input("PILIH MENU: ")

                if pilihan_warung == '1':
                    warung.input_transaksi("JUAL")
                elif pilihan_warung == '2':
                    warung.input_transaksi("BELI")
                elif pilihan_warung == '3':
                    warung.tampilkan_semua_transaksi()
                elif pilihan_warung == '4':
                    print(f"TOTAL PEMASUKAN: {warung.total_pemasukan()}")
                elif pilihan_warung == '5':
                    print(f"TOTAL PENGELUARAN: {warung.total_pengeluaran()}")
                elif pilihan_warung == '6':
                    print(f"SALDO AKHIR: {warung.saldo_akhir()}")
                elif pilihan_warung == '7':
                    break
                else:
                    print("PILIHAN TIDAK VALID, SILAHKAN PILIH MENU YANG SESUAI.")

        elif pilihan == '4':
            print("TERIMA KASIH!")
            break

        else:
            print("PILIHAN TIDAK VALID, SILAHKAN PILIH MENU YANG SESUAI.")

if __name__ == "__main__":
    main()
