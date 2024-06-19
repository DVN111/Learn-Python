

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