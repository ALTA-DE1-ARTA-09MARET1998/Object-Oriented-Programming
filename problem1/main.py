# tulis solusi code disini
import math

class Persegi():
    def __init__(self, sisi):
        self.sisi = sisi

    def luas (self):
        return (round(self.sisi * self.sisi))
    
    def keliling (self):
        return (round(4 * self.sisi))
    
class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas (self):
        return (round(0.5 * (self.alas * self.tinggi)))
    
    def keliling (self):
        kemiringan = math.sqrt(self.alas ** 2 + self.tinggi ** 2)
        return (round(self.alas + self.tinggi + kemiringan))


class Persegi_panjang():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return (round(self.panjang * self.lebar))
    
    def keliling(self):
        return (round(2 * (self.panjang + self.lebar)))

if __name__ == "__main__":
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = Persegi_panjang(7, 8)

    print("Luas")
    print("Persegi:", persegi.luas())
    print("Segitiga:", segitiga.luas())
    print("Persegi Panjang:", persegi_panjang.luas())

    print("\nKeliling")
    print("Persegi:", persegi.keliling())
    print("Segitiga:", segitiga.keliling())
    print("Persegi Panjang:", persegi_panjang.keliling())