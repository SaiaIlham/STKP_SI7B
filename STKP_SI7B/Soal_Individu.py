
import os, re
import time
mulai = time.time()

jumlah = 0
for suffix in range (1,1000000):
    jumlah = jumlah + suffix
    print("Jumlah ke-", suffix, "hasil", jumlah)

selesai = time.time()

print("Hasil", jumlah)
print(selesai-mulai)
