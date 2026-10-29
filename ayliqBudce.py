gelir=float(input())
xercler=float(input())
if gelir<0 or xercler<0:
    print("Gelir menfi ola bilmez")
elif gelir==0:
    print("Xəta: Gəlir 0 ola bilməz, faiz və balans hesablanmır.")
else:
    if xercler>gelir:
        print("Büdcə kəsiriniz var")
    elif xercler>=gelir*0.8:
        print("Xərclərə diqqət et")
    elif xercler>0.5*gelir and xercler<0.8*gelir:
        print("Büdcə normaldır")
    else:
        print("Yaxşı qənaət edirsiniz")
    print("Qalan pul miqdarı=", gelir-xercler)
    print("Qənaət faizi:", ((gelir-xercler)/gelir)*100, "%")