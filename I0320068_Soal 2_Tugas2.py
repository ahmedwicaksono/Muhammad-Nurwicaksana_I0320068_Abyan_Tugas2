nama = "Muhammad Nurwicaksana"
nim = "I0320068"
jenis_kelamin = "Laki-laki"
prodi = "Teknik Industri"
angkatan = 2020
tempat_lahir = "Surakarta"
tgl_lahir = "16 Januari 2003"
tlahir = 16
blahir = 1
Tlahir = 2003
lahir = tlahir+(blahir*30)+(Tlahir*365)
tanggal_sekarang = 13
bulan_sekarang = 3
Tahun_sekarang = 2021
sekarang = tanggal_sekarang+(bulan_sekarang*30)+(Tahun_sekarang*365)
tahun = int((sekarang-lahir)/365)
bulan = int(((sekarang-lahir)%365)/30)
hari = int(((sekarang-lahir)%365)%30)
alamat = "Jl.Kutai Raya No.10 Sumber,Banjarsari,Surakarta"
lingkungan = "Rumah saya depan rumah pak presiden"
berat_badan = 97
tinggi_badan = 171
us_sepatu = 9.5
makanan_favorit = "Magelangan"
minuman_favorit = "Air es"
hobi = "Game"
print("Nama saya",nama,"dan saya adalah seorang",jenis_kelamin)
print("Saya adalah seorang mahasiswa",prodi,"angkatan",angkatan,"dengan NIM",nim)
print("Alamat saya berada di",alamat)
print("Saya lahir di",tempat_lahir,"pada",tgl_lahir,"dan sekarang berumur",tahun,"tahun",bulan,"bulan",hari,"hari")
print(lingkungan)
print("Hobi saya adalah",hobi)
print("Berat badan saya",berat_badan,"kg, dan","tinggi saya",tinggi_badan,"cm")
print("Ukuran sepatu saya US",us_sepatu)
print("Makanan favorit saya",makanan_favorit,"dan minuman favorit saya",minuman_favorit)