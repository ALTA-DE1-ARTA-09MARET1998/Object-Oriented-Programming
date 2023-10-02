# tulis solusi code disini
import math

class Ongkos():
    def __init__ (self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def volume_brg (self):
        return (round(self.panjang * self.lebar * self.tinggi))
    
    def ongkir(self):
        volume = self.volume_brg()
        # bayar = berat_bulat * 5000
        if volume <= 50:
            return 5000
        elif volume > 50:
            return 
    
        # berat_bulat = round(self.berat)
        # bayar = berat_bulat * 5000

        if volume == 50 and berat_bulat == 1:
            return 5000
        elif volume > 50 and berat_bulat >= 1:
            return bayar
        else:
            return None

if __name__ == "__main__":
    volume = Ongkos(5, 2, 4, 1)

    print("Harga: ", volume.ongkir())