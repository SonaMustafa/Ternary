tecrubeIli=int(input("Təcrübə illərinizi daxil edin: "))
texnikiMusahibeBali=int(input("Texniki müsahibə balınızı daxil edin: (0-100): "))
if tecrubeIli<0 or texnikiMusahibeBali<0 or texnikiMusahibeBali>100:
    print("Yanlış məlumat daxil edildi.") 
else:
    if texnikiMusahibeBali>=90:       
        print("Siz güclü namizədsiz")
    elif tecrubeIli>=2 and texnikiMusahibeBali>=70:
        print("Növbəti mərhələyə dəvət olunursunuz.")
    else:
        print("Namizəd uyğun deyil")
    status = "Növbəti mərhələyə keçdiniz" if (texnikiMusahibeBali >= 90 or (tecrubeIli >= 2 and texnikiMusahibeBali >= 70)) else "Mərhələni keçmədiniz"
    print(status)
    