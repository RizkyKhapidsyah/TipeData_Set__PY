# Contoh 1
print("=" * 5, "CONTOH 1", "=" * 5)
# Tipe Data: Set (Himpunan) :
StokMobil = {"Toyota",
             "Kijang",
             "Karimun",
             "Daihatsu"}

StokMobil.add("Hyundai")
StokMobil.add("Daihatsu") # Tidak akan ditambahkan karena terdapat nama yang sama 
StokMobil.add("Daihatsuu")

print(StokMobil)
print("\n")

# Contoh 2
print("=" * 5, "CONTOH 2", "=" * 5)
Kendaraan = set()

Kendaraan.add("Sepeda")
Kendaraan.add("Mobil")
Kendaraan.add("Pesawat")
Kendaraan.add("Kapal Laut")
Kendaraan.add("Dokar")

print(Kendaraan)
print(sorted(Kendaraan))
print("\n")

# Contoh 3
print("=" * 5, "CONTOH 3", "=" * 5)
Barang = set()

Barang.add("Tang")
Barang.add("Obeng")
Barang.add("Martil")
Barang.add("Pencabut Paku")
Barang.add("Kayu")
Barang.add(12345)

print(Barang)
# print(sorted(Barang)) # Akan terjadi runtime Error di baris ini Karena data set Barang ada yang berisi integer (12345)
# print(Barang[2]) # Akan Error Karena tipedata set tidak mendukung indexing sebagaimana List
print("\n")

# Contoh 4
print("=" * 5, "CONTOH 4", "=" * 5)

Bilangan_Ganjil = {1, 3, 5, 7, 9}
Bilangan_Genap = {2, 4, 6, 8, 10}
Bilangan_Prima = {2, 3, 5, 7}

print(Bilangan_Ganjil.union(Bilangan_Genap))
print(Bilangan_Ganjil.intersection(Bilangan_Genap)) # Tidak akan mengeluarkan apa-apa
print(Bilangan_Ganjil.intersection(Bilangan_Prima)) 


# NB: Untuk menjalankan aplikasi tambahkan tanda comment (#) pada awal baris yang sudah tahu bahwa baris tersebut akan error.