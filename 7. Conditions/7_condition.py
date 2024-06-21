# kondisi dapat dilakukan dengan membandingkan sebuah variable
x1 = 10 
x2 = "sepuluh"
kondisi = x1==10
if kondisi:
    print(f'apakah benar variabel x=10. = {kondisi}')

# coba gunakan operator and, or dan in dalam kondisi 

print(f"apakah x1=10 dan x2='sepuluh' = {x1==10 and x2=="sepuluh":}")
x2="dua"
print(f"apakah x1=10 dan x2='sepuluh' = {x1==10 and x2=="sepuluh":}")

# or
name = "dani"
print(f"apakah namamu dani atau rehan = {name=="dani" or name=="rehan"}")

# in
# fungsi ini biasasnya digunakan untuk mengecek sebuah itemstring dalam list
daftarNama = ["adi","otong","rafi","joni"]
daftarNama2 = ["adi","otong","rafi","joni"]
print(f"apakah ada orang yan bernama otong dalam daftar nama?.({"otong" in daftarNama})")


# coba gunakan fungsi if, elif dan else 

# jika memnuhi kondisiif
print("jika memenuhi kondisi if")
if "otong" and "joni" in daftarNama:
    print("kondisi if terpenuhi")
elif "otong" and "joni" in daftarNama2:
    print("ada orang yang bernama otong dan joni dalam daftar nama 2")
else:
    print("dua duanya gaada njir")

print("jika memenuhi kondisi elif")
if "zaki" and "fata" in daftarNama:
    print("kondisi if erpenuhi")
elif "otong" or "joni" in daftarNama2:
    print("kondisi elif terpenuhi")
else:
    print("dua duanya gaada njir")
    
print("jika memenuhi kondisi else")
if "zaki" and "fata" in daftarNama:
    print("")
elif "zaki" and "fata" in daftarNama2:
    print("ada orang yang bernama otong dan joni dalam daftar nama 2")
else:
    print("kondisi else terpenuhi")
    
# sekarang coba gunakan operator is
# ini digunakan untuk membandingkan antara variabel atau list

# antar variabel 
v1 = 2
v2 = 2

print(f"apakah v1 is v2? ({v1 is v2})")


# coba bandingkan antara 2 list 
list1 = [1,2,3]
list2=[1,2,3]

print(f"apakah antara {list1} dan {list2} adalah sama = {list1 is list2}")
# hasilnya ialah false, ha ni karna operator "is" tidak 
# mencocokkan nilai dari variablenya melainkan instance nya


# sekarang coba operator not
buah = ["apel","jeruk","melon"]

# 
print(f"apakah buah apel tidak termasuk buah ({buah[0] not in buah})")