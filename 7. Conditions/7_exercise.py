angka1 = 16
angka2 = 0
list1 = [1,2,3] 
list2=[1,2]

# anka pertama harus lebih dari > 15
if angka1>15:
    print(f"angaka pertama lebih dari 15 = ({angka1>15})")

# cek apakah list1 ada
if list1 is not True: # list yang kosog dianggap tidak valid oleh python
    print(f"list1 tidak valid")

if list2:
    print(f"list2 valid")
    
# cek apakah panjag/ jumlah item dalam list kedua = 2
if len(list2) == 2:
    print(f"apakah ada 2 item dalam list2? ({len(list2)==2})")
    
# cek apakah list1 + list 2 == 5 
if len(list1) + len(list2) == 5:
    print(f"ya, panjang list1({list1}) + panjang list2({list2}) == 5 ({len(list1)+len(list2)==5})")
    
# cek apakah angka 2 valid atau tidak
if not angka2:
    print(f"angka 2 tidak valid")