# # looping biasanya digunakan untuk mengiterasi setiap item yang berada dalam list
# listAngka = [1,2,3,4,5]
# # kia dapat menggunakan fungsi for
# indeks = 0
# for angka in listAngka:
#     print(f"{angka} berada pada indeks ke {indeks} dalam list angka")
#     indeks+=1
    
# # coba menggunakan fungsi range(<angka integer>)
# # contohnya misal kita ingin memprint angka 1-5
# # for x in range(5):
# #     print(x)
# # kita juga bisa megatur awal dan akir dari rangenya dengan 

# for x2 in range(2,4): # nilai yang dicetk adalah 2,3. sistemnya sama seperti >= a and < b
#     print(x2)




# coba fungsi while
# fungsi while adalah perulangan dengan batasan sebuah kondisi 
# listJadwalSholat = ["Subuh", "Dzuhur", "Ashar", "Maghrib", "Isya"]
# indexSholat = 0 # karna ini tiaabel iterator seperti pada fungsi for, maka perlu membuat variabel iterator

# while indexSholat < len(listJadwalSholat): # pastikanika ingin mengiterasi sebuah list, gunakan panjangdari list yang akan diiterasi
#     print(listJadwalSholat[indexSholat])
#     indexSholat+=1
    
'''output = 
Subuh
Dzuhur
Ashar
Maghrib
Isya'''

# for x in range(10): # ini akan mengahasilkan 0,1,2,3,4,5,6,7,8,9
#     if x % 2 == 0: # cek apakah nilai x saat ini genap
#         continue # jika iya, maka langsung anjut ke iterasi seanjutnya tanpa menjalankan kode seetalh ini 
#     print(x) # jika tidak, print nilai x ada iterasi saat ini
    
for i in range(1, 10):
    # if(i%5==0):
    #     break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    