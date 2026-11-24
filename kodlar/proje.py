def renksec(renk):
    print(f"{renk} seciniz:\n ")
    Kirmizi = int(input("Kirmizi (0-255): "))
    Yesil = int(input("Yesil (0-255): "))
    Mavi = int(input("Mavi (0-255): "))
    return Kirmizi, Yesil, Mavi


def secim():
    print("Hangi sekli olusturmak istersiniz?\n")
    print("1-Satranc Deseni")
    print("2-Cizgili Desen")
    print("3-Gradyan Geçiş Deseni")
    print("4-Yatay 3 Şeritli Bayrak")
    print("5-Daire Deseni\n")


    desen = int(input("Karar: "))
    return desen

desen = secim()

yukseklik = int(input("Yukseklik (Pixel): "))
genislik = int(input("Genislik (Pixel): "))

with open("buyuk.ppm", "w") as dosya:
    dosya.write("P3\n")
    dosya.write(f"{genislik} {yukseklik}\n")  
    dosya.write("255\n")

    if(desen == 1):
        Kirmizi1, Yesil1, Mavi1 = renksec("1. Renk")
        Kirmizi2, Yesil2, Mavi2 = renksec("2. Renk")
    
        for satir in range(yukseklik):
            for sutun in range(genislik):
                if((satir + sutun)%2==0):
                    dosya.write(f"{Kirmizi1} {Yesil1} {Mavi1} ")
                else:
                    dosya.write(f"{Kirmizi2} {Yesil2} {Mavi2} ")

            dosya.write("\n")
    
    elif(desen == 2):
        Kirmizi1, Yesil1, Mavi1 = renksec("1. Renk")
        Kirmizi2, Yesil2, Mavi2 = renksec("2. Renk")
    
        for satir in range(yukseklik):
            for sutun in range(genislik):
                if(satir%2==0):
                    dosya.write(f"{Kirmizi1} {Yesil1} {Mavi1} ")
                else:
                    dosya.write(f"{Kirmizi2} {Yesil2} {Mavi2} ")

            dosya.write("\n")
    elif(desen == 3):
        Kirmizi1, Yesil1, Mavi1 = renksec("1. Renk")
        Kirmizi2, Yesil2, Mavi2 = renksec("2. Renk")
    
        for satir in range(yukseklik):
            for sutun in range(genislik):
                oran = sutun/(genislik-1)
                
                Kirmizi = int(Kirmizi1+(Kirmizi2-Kirmizi1)*oran)
                Yesil = int(Yesil1 + (Yesil2-Yesil1)*oran)
                Mavi = int(Mavi1 + (Mavi2-Mavi1)*oran)
                
                dosya.write(f"{Kirmizi} {Yesil} {Mavi} ")

            dosya.write("\n")
    elif(desen == 4):
        Kirmizi1, Yesil1, Mavi1 = renksec("1.Renk")
        Kirmizi2, Yesil2, Mavi2 = renksec("2.Renk")
        Kirmizi3, Yesil3, Mavi3 = renksec("3.Renk")

        for satir in range(yukseklik):
            for sutun in range(genislik):
                if satir<yukseklik // 3 :
                    dosya.write(f"{Kirmizi1} {Yesil1} {Mavi1} ")
                elif satir< 2 * yukseklik // 3:
                    dosya.write(f"{Kirmizi2} {Yesil2} {Mavi2} ")
                else:
                    dosya.write(f"{Kirmizi3} {Yesil3} {Mavi3} ")
            dosya.write("\n ")
    elif(desen == 5):
        print("Kendin değer gir veya resime göre oranla:")
        print("1-Oranla")
        print("2-Kendin gir\n")

        

        
        oran = float(input("Oran kaç olsun (0-1): "))

        kucukKenar = min(yukseklik,genislik)

        merkezYukseklik = (yukseklik-1)/2
        merkezGenislik = (genislik-1)/2
        
        Kirmizi1, Yesil1, Mavi1 = renksec("1.Renk")
        Kirmizi2, Yesil2, Mavi2 = renksec("2.Renk")

            
        for satir in range(yukseklik):
            for sutun in range(genislik):
                    
                uzaklik = ((satir-merkezYukseklik)**2+(sutun-merkezGenislik)**2)**0.5
                    
                if(uzaklik< kucukKenar/2*oran):
                    dosya.write(f"{Kirmizi1} {Yesil1} {Mavi1} ")
                else:
                    dosya.write(f"{Kirmizi2} {Yesil2} {Mavi2} ")
            
            dosya.write("\n")
                        
        


