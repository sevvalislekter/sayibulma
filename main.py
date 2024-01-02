

def sayi():
    sayilar=[]
    for i in range(1,4):
        sayi1=int(input("sayi girin"))
        sayilar.append(sayi1)
    enb(sayilar)

def enb(liste):
    sayib=liste[0]
    for i in liste:
        if i>sayib:
            sayib=i

        else:
            sayib
    goruntu(sayib)
def goruntu(x):
    print("en buyuk sayı",x)


print(sayi())