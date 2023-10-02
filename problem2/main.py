# tulis solusi code disini

import math

class Kubus ():
    def __init__ (self, sisi):
        self.sisi = sisi

    def Volume (self):
        return (round(self.sisi ** 3))
    
class Balok ():
    def __init__ (self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def Volume (self):
        return (round(self.panjang * self.lebar * self.tinggi))
    
class Tabung():
    def __init__ (self, phi, jari, tinggi):
        self.phi = phi
        self.jari = jari
        self.tinggi = tinggi

    def Volume (self):
        return(round(self.phi * self.jari ** 2 * self.tinggi))

if __name__ == "__main__":
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(3.14,7, 10)

    print ("Volume")
    print ("Kubus:", kubus.Volume())
    print ("Balok:", balok.Volume())
    print ("Tabung:", tabung.Volume())