toplam=0
while True:
    print('bir sayı giriniz, çıkış için 0(sıfır)')
    girilen=int(input("sayi: "))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print(toplam)
