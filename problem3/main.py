# tulis solusi code disini
class Penjumlahan():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tambah(self):
        return self.a + self.b
    
class Pengurangan():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kurang(self):
        return self.a - self.b

class Perkalian():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kali(self):
        return (round(self.a * self.b))
    
class Pembagian():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def bagi(self):
        if self.b == 0:
            return "Tidak bisa melakukan pembagian dengan 0."
        return (round(self.a / self.b))
    
if __name__ == "__main__":
    tambah = Penjumlahan(3,4)
    kurang = Pengurangan(15,4)
    kali = Perkalian(10,10)
    bagi = Pembagian(12,3)
    
    print("Penjumlahan:", tambah.tambah())
    print("Pengurangan:", kurang.kurang())
    print("Perkalian:", kali.kali())
    print("Pembagian:", bagi.bagi())