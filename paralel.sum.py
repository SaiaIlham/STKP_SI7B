import os,re, threading
import time

class jumlah(threading.Thread):
    def__init__(self,awal,akhir):
        threading.Thread.__init__(self)
        self.awal=awal 
        self.akhir=akhir
    def run(self):
        self.hasil=0
        for suffix in range (self.awal, self.akhir+1):
            self.hasil = self.hasil = suffix
            print(self.suffix, "=", self_hasil)
    def hasil(self):
        return self.hasil

start = time.time()

hitung1=jumlah(1, 5000000)
print(hitung1.awal)
print(hitung1.akhir)
end = time.time()
print(end-start)
