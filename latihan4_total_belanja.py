# Latihan 4: Menghitung total belanja dengan PPN 11%

nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan (Rp): "))
jumlah = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah
ppn = subtotal * 0.11
total = subtotal + ppn

print(f"Subtotal : {subtotal}")
print(f"PPN 11%  : {ppn}")
print(f"Total    : {total}")
