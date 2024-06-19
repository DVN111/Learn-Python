def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
def build_sentence(info):
    return info + " is a benefit of functions!"

def Subission():
    # fungsi list_benefits mengembalikan sebuah list ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"], 
    # maka dari itu list itu harus disimpan kedalam sebuah variabel supaya nilanya dapat diakses
    listB = list_benefits()
    
    for benefit in listB: # lakukan iterasi pada setiap item dalam variabel yang tadi menampung list yang dikembalikan dari fungsi list_benefits
        print(build_sentence(benefit)) # setiap item yang di iterasi kemudian dijadikan sebagai argumen untuk fungsi build_sentence(info)

Subission()