astring = "bismillah lancar"

# coba ambil kata illah menggunakan slicing [::]
print("ambil huruf pada indeks ke 4 -> terakhir dari string = "+ astring[4:]) # ini mengambil indeks ke 4 -> terakhir dari kata bismillah

# cara membalika urutan string menggunakan step pada slicing [::-1]
print("kata bismillah lancar setelah dibalik = "+astring[::2]) # maksud 2 pada step adalah dia akan memprint indeks ke i + 2, 

# kapitalisasi strin menggunakan sebuah fungsi upper() dan lower()
# caranya ialah <variabel string>.upper() / <variabel string>.lower()
print("ini menggunakan fungsi lower() = "+astring.lower())
print("ini menggunakan fungsi upper() = "+astring.upper())

# menggunakan fungsi startwith("<kata/kalimat>") untuk mengecek apakah string dimula dengan kaa/kalimat tersebut
print(f"apakah string dimulai dengan kata bismillah = {astring.startswith("bismillah")}")
print(f"apakah string diakhiri dengan kata sukses = {astring.endswith("sukses")}")
print(f"apakah string diakhiri dengan kata lancar = {astring.endswith("lancar")}")

# pisahkan kalimat bismillah lancar menjadi 2 yang dipisahkan oleh " "
# pemisahan kalimat dengan menggunakan " " sebgaia pemisahnya dapat menggunakan fungsi <variabel string>.split("<karakter yang memisahkan tiap kata>")
astring2 = "kata1 kata2 kata3"
astring2_terpisah = astring2.split(" ")
print(f"setelah dipisah, kalimat dalam variabel astring2 akan menjadi {astring2_terpisah}")














