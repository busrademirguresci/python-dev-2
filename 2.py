stokMiktari=10000
satilanUrun=500
alinanUrun=100
i=0
while True:
    stokMiktari=stokMiktari-satilanUrun+alinanUrun
    i=i+1
    if(stokMiktari<=0):
        print(i,"ayda stoğunuz sıfırlanmıştır")
        break
