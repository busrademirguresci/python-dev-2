gunluk_uretilen=200
defolu_urun=0
toplam_defolu_urun=0
i=0
while (defolu_urun<=gunluk_uretilen*0.20):
    defolu_urun=int(input('defolu ürün miktarı:'))
    toplam_defolu_urun=toplam_defolu_urun+defolu_urun
    i=i+1
    if(defolu_urun>=gunluk_uretilen*0.20):
        print("defolu ürün sayısı limiti aştı")
        break
    print(i,"günlük","defolu ürün sayısı:",toplam_def_urun)
