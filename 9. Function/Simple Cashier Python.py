

menu_makanan = [(1,"pancong vanilla",7000), (2,"nasi bakso",10000)]
menu_minuman = [(1,"kopi susu",12000),(2,"cold brew", 8000)]
total_menu = []

def welcoming_massage():
    print(f"Hello Wellcome to Kopi Studio 24 app")
    
def pilih_menu_makanan():
     total_harga = 0
     while True:
        print("\n== Menu Makanan ==")
        for no, makan, harga in menu_makanan:
            print(f"{no}. {makan} (Rp {harga})")
        print("\n== Menu Minuman ==")
        for no, minum, harga in menu_minuman:
            print(f"{no}. {minum} (Rp {harga})")
        print("0. Selesai dan Cetak Pesanan")

        try:
            menu_dipilih = int(input("Menu apa yang ingin dipesan? [1/2/0]: "))
            if menu_dipilih == 0:
                for item in total_menu:
                    print(f"{item[0]}. {item[1]} (Rp {item[2]})")
                    total_harga = total_harga + item[2] 
                print(f"total harga = {total_harga}")
                return total_menu,total_harga
                break
            elif menu_dipilih in [1, 2]:
                total_menu.append(menu_makanan[menu_dipilih - 1])
            elif menu_dipilih in [3, 4]:
                total_menu.append(menu_minuman[menu_dipilih - 3])
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor menu yang benar.")
    
def Cetak(kasir,cust, tipe, total_menu,total_harga,kembalian):
    print(f"{tipe}")
    print(f"Staff     : {kasir}")
    print(f"Customer  : {cust}")
    print(f"=============================================")
    for item in total_menu:
        print(f"{print(f"{item[0]}. {item[1]} : {item[2]}")}")
    print(f"=============================================")
    print(f"Total harga = {total_harga}")
    print(f"Payment : {tipe}\n{kembalian}")
    
welcoming_massage()
kasir_name= input("Masukkan nama kasir : ")
cust_name = input("Masukkan nama customer : ")
tipe = input("Masukkan tipe memakan : [dine in/ take away]")
total_menu, total_harga = pilih_menu_makanan()
uang_kustomer = int(input("Berapa uang yang dibayarkan customer? = "))
kembalian = total_harga-uang_kustomer
Cetak(kasir_name,cust_name,tipe,total_menu,total_harga,kembalian)






# def IntroductionMassage():
#     print(f"Hello {cusName}, welcome to DVNL Official Store")

# def SuccesfullPayment():    
#     print(f"Thank you for your order ({cusName})")
    
# def SuccesfullPayment():    
#     print(f"Thank you for your order, {cusName}. Here are the details of your order:")
#     for index, pakaian in enumerate(dataCloth,start=1):
#         print(f"Item {index}: {pakaian[0]} (Ukuran: {pakaian[1]}, Warna: {pakaian[2]}) Jumlah: {pakaian[3]} pcs")
        

# def InputItem():
#     cloth_name=input("Masukkan Nama Pakaian: ")
#     cloth_size=input("Masukkan ukuran Pakaian: ")
#     cloth_color=input("Masukkan warna pakaian: ")
#     cloth_number=input("Masukkan jumlah pakaian: ")
#     list_data_pakaian=[cloth_name, cloth_size, cloth_color,cloth_number]
#     return list_data_pakaian

# dataCloth=[]


# def ItemCollection():
#     print("apa yang mau dipesan? masukkan data pakaian:")
#     indeks=0
#     while indeks >=0:
#         pakaian = InputItem()
#         dataCloth.append(pakaian)
#         print(pakaian)
        
#         lanjut=input("ada lagi yang mau dipesan: ").lower()
        
#         if lanjut =="y":
#             indeks+=1
#         else:
#             break
            
            
            
    
    
# # program start
# cusName = input("Masukkan nama customer")
# IntroductionMassage()
# ItemCollection()
# SuccesfullPayment()