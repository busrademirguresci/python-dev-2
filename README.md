# python-dev-2
odev-sorusu-1
#a=toplamsatismiktari
#b=hammaddemaliyeti
#c=bakimonarimgiderleri
#d=sevkiyatgiderleri
#e=satinalinanhizmetgiderleri
def katmadegerciro(a,b,c,d,e):
    global katmadegerciro
    katmadegerciro=a-(b+c+d+e)
    if(katmadegerciro>1000):
        print("işletme katma değer cirosu yüksek")
    elif(500<katmadegerciro<999):
        print("işletme katma değer cirosu normal")
    else:
        print("işletme katma değer cirosu düşük")
        return katmadegerciro
print("lütfen değerleri giriniz")
a=int(input("toplamsatismiktari:"))
b=int(input("hammaddemaliyeti:"))
c=int(input("bakimonarimgiderleri:"))
d=int(input("sevkiyatgiderleri:"))
e=int(input("satinalinanhizmetgiderleri:"))
sonuc=katmadegerciro(a,b,c,d,e)
print(sonuc)




odev-sorusu-2
#x=2016yili,y=2017yili,a=mustericalismasuresi, w=calisilansure,t=toplammusterimiktari
def musterilerleCalismaSuresi2016yiliHesapla(w,t):
    global a
    a=w/t
    return a
def musterilerleCalismaSuresi2017yiliHesapla(w,t):
    global z
    z=(w+50)/(t+20)
    return z
t=50
w=170
x=musterilerleCalismaSuresi2016yiliHesapla(w,t)
y=musterilerleCalismaSuresi2017yiliHesapla(w,t)
print (x-y)




odev-sorusu-3
def ilkAltiAylikKar(yazilimGelir,finansmanGelir,urunSatisGelir,calisanMaaslari,kiraGideri,donanımMaliyeti):
    global ilkAltiAylikKar
    ilkAltiAylikKar=(yazilimGelir+finansmanGelir+urunSatisGelir)-(calisanMaaslari+kiraGideri+donanımMaliyeti)
    return ilkAltiAylikKar
def sonAltiAylikKar(yazilimGelir,sponsorlukGeliri,eTicaretGeliri,urunSatisGelir,calisanMaaslari,kiraGideri,bakimMaliyeti):
    global sonAltiAylikKar
    sonAltiAylikKar=(yazilimGelir+sponsorlukGeliri+eTicaretGeliri+urunSatisGelir)-(calisanMaaslari+kiraGideri+bakimMaliyeti)
    return sonAltiAylikKar
print("Lütfen Değerleri Giriniz")
yazilimGelir=int(input("yazılım geliri giriniz:"))
finansmanGelir=int(input("finansman gelirini giriniz:"))
urunSatisGelir=int(input("ürün satış geliri giriniz:"))
calisanMaaslari=int(input("çalışan maaşları giriniz:"))
kiraGideri=int(input("kira gideri giriniz:"))
donanımMaliyeti=int(input("donanım maliyeti giriniz:"))
sponsorlukGeliri=int(input("sponsorluk geliri giriniz:"))
eTicaretGeliri=int(input("e ticaret geliri giriniz:"))
bakimMaliyeti=int(input("bakım maliyeti giriniz:"))
x=ilkAltiAylikKar(yazilimGelir,finansmanGelir,urunSatisGelir,calisanMaaslari,kiraGideri,donanımMaliyeti)
y=sonAltiAylikKar(yazilimGelir,sponsorlukGeliri,eTicaretGeliri,urunSatisGelir,calisanMaaslari,kiraGideri,bakimMaliyeti)
if (ilkAltiAylikKar-sonAltiAylikKar>5000):
    print("işletme çok karlı")
elif(1000<ilkAltiAylikKar-sonAltiAylikKar<5000):
    print("işletme karı normal")
else:
    print("işletme yeterince karda değil")
    
    
    
    
    
    
odev-soru-4
satilanKoltukSayisi=int(25)
satilanYatakSayisi=int(20)
satilanDolapSayisi=int(10)
alinanKoltukSayisi=int(10)
alinanYatakSayisi=int(15)
alinanDolapSayisi=int(5)
def donembasiStok(koltukSayisi,yatakSayisi,dolapSayisi):
    global donembasiStok
    donembasiStok=koltukSayisi+yatakSayisi+dolapSayisi
    return donembasiStok
def donemsonuStok(satilanKoltukSayisi,satilanYatakSayisi,satilanDolapSayisi,alinanKoltukSayisi,alinanYatakSayisi,alinanDolapSayisi):
    global donemsonuStok
    donemsonuStok=(donembasiStok-(satilanKoltukSayisi+satilanYatakSayisi+satilanDolapSayisi)+(alinanKoltukSayisi+alinanYatakSayisi+alinanDolapSayisi))
    return donemsonuStok
def ortalamaStok(donembasiStok,donemsonuStok):
    global ortalamaStok
    ortalamaStok=((donembasiStok+donemsonuStok)/2)
    return ortalamaStok
print('lütfen stoklarınızı giriniz')
koltukSayisi=int(input("koltuk sayısı giriniz:"))
yatakSayisi=int(input("yatak sayısı giriniz:"))
dolapSayisi=int(input("dolap sayısı giriniz:"))
x=donembasiStok(koltukSayisi,yatakSayisi,dolapSayisi)
y=donemsonuStok(satilanKoltukSayisi,satilanYatakSayisi,satilanDolapSayisi,alinanKoltukSayisi,alinanYatakSayisi,alinanDolapSayisi)
z=ortalamaStok(donembasiStok,donemsonuStok)
z=(x+y)/2
print(z)


