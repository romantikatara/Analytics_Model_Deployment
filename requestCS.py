# Import Libraries
import requests

# URL yang digunakan
url = 'http://localhost:5000/api'

# Menentukan nilai dari setiap features yang dibutuhkan untuk melakukan test pada model yang telah dibuat
r = requests.post(url,json={'AGE' : 32,
                           'MARRIAGE' : 2,
                           'PAY_1' : 0,
                           'PAY_2' : 2,
                           'PAY_3' : 1})
print(r.json())

#print('Input data diri nasabah yang mengajukan kredit')
#S = print('Input jenis kelamin nasabah (1 = Pria, 2 = Wanita) : ')
#A = print('Input usia nasabah : ')
#M = print('Input status nasabah (1 = Belum Menikah, 2 = Menikah, 3 = Lainnya) : ')
#E = print('Input pendidikan nasabah (1 = S2/S3, 2 = Diploma/S1, 3 = SMA, 4 = Lainnya) : ')
#P1 = print('Input pembayaran ke-1 nasabah (0 = Tepat waktu, 1 = Terlambat 1 bulan, dst) : ')
#P2 = print('Input pembayaran ke-2 nasabah (0 = Tepat waktu, 1 = Terlambat 1 bulan, dst) : ')
#P3 = print('Input pembayaran ke-3 nasabah (0 = Tepat waktu, 1 = Terlambat 1 bulan, dst) : ')