"""
Program Menghitung Luas Segitiga
luas_segitiga=alas * tinggi / 2
"""

alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMembuat fungsi menghitung luas segitiga')
def hitung_luas_segtiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Ini luas segitiga pertama = {hitung_luas_segtiga(10, 2)}')
print(f'Ini luas segitiga pertama = {hitung_luas_segtiga(20, 2)}')