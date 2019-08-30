print("selamat datang di LinkAja")
print("#pakeLinkAja")


print ()

dict ={"saldo":1500000}

def start () :
    menu =input("silahkan pilih menu berikut ini! \n1.info saldo \n2.debit atau kredit \n= ")
    if menu == "1":
        info()
    
    elif menu =="2" :
        menu2()
    
    else:
        print("mohon untuk memilih yang ada pada daftar")
        print("----------------------------------------")
        start()

def exit () :
    print("-------------------------------------")
    print("terima kasih telah menggunakan layanan Link Aja")
    print("-------------------------------------")

def info () :
    print("-------------------------------------")
    print("jumlah saldo anda = Rp. ",dict["saldo"])
    print("-------------------------------------")

    menusaldo = input("ingin melakukan transaksi lainnya \n1.ya \n2.tidak \n= ")
    if menusaldo == "1" :
        start()
    elif menusaldo == "2" :
        exit ()

def menu2() :
    menu = input("sialhkan memilih transaksi \n1.debit \n2.kredit \n=")
    if menu == "1":
        #debit
        nom = input("masukan nominal \nRp.")
        current = dict["saldo"] + int(nom)
        print ("saldo anda sekarang \nRp =", current)
        exit()

    elif menu == "2":
        #kredit
        nom2 = input("masukan nominal \nRp.")
        current2 = dict["saldo"] - int(nom2)
        if int(nom2) > dict["saldo"] :
            print("-------------------------------")
            print("Maaf saldo anda tidak memenuhi")
            print("-------------------------------")

        else :
            print("--------------------------")
            print("anda menggunakan kredit sebesar \nRp.",nom2)
            print("saldo anda sekarang \nRp.",current2)
            print("--------------------------")
            exit()
        
    else :
        print("-------------------------")
        print("silahkan pilih 1 atau 2")
        print("-----------------------")
        menu2()

start()





        















