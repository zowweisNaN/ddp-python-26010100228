# Latihan 2: Menghitung luas dan keliling persegi panjang

panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas     : {luas} m2")
print(f"Keliling : {keliling} m")

"""
Trace Table (contoh: panjang = 8, lebar = 5)
-------------------------------------------------
Baris | panjang | lebar | luas | keliling | Output
-------------------------------------------------
  2   |   8.0   |       |      |          |
  3   |   8.0   |  5.0  |      |          |
  5   |   8.0   |  5.0  | 40.0 |          | Luas : 40.0 m2, Keliling : 26.0 m
  6   |   8.0   |  5.0  | 40.0 |  26.0    | Luas : 40.0 m2, Keliling : 26.0 m
-------------------------------------------------
"""
