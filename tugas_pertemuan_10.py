
# =====================================
# 1. TUPLE DAN SET
# =====================================

# a. Membuat tuple mahasiswa
mahasiswa = ("Wahyu Putra Wibawa", "2605060078", "Teknologi Informasi")
print("Data Mahasiswa:", mahasiswa)

# b. Menampilkan NIM dan Prodi
print("NIM:", mahasiswa[1])
print("Prodi:", mahasiswa[2])

# c. Mencoba mengubah isi tuple
# Baris ini akan menghasilkan error jika dijalankan
# mahasiswa[2] = "Teknologi Informasi"

# d. Membuat set nilai angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Nilai Angka:", nilai_angka)


# =====================================
# 2. MANIPULASI DICTIONARY
# =====================================

# a. Membuat dictionary mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

print("\nData Awal:", data_mahasiswa)

# b. Mengubah prodi dan menambahkan angkatan
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026

print("Setelah Diubah:", data_mahasiswa)

# c. Menghapus data NIM
del data_mahasiswa["nim"]

# Menampilkan hasil akhir
print("Data Mahasiswa Akhir:", data_mahasiswa)


# =====================================
# 3. PERULANGAN PADA DICTIONARY
# =====================================

# a. Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Menampilkan barang dan harganya
print("--- Daftar Harga Buah ---")

for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")

# c. Menghitung total belanja
total_belanja = 0

for harga in keranjang.values():
    total_belanja += harga

print("-------------------------")
print("Total Belanja: Rp", total_belanja)
