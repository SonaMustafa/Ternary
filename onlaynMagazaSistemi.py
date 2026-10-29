mebleg=float(input("Məbləği daxil edin: "))
if mebleg<0:
    print("Mənfi məbləğ daxil etdiniz")
else:
    print("Endirim qazandınız") if mebleg>=100 else print("Endirim yoxdur")
    if mebleg>=200:
        mebleg-=(mebleg*0.2)
    elif mebleg>=100 and mebleg<=199.99:
        mebleg-=(mebleg*0.1)
    print("Yekun məbləğ: ", mebleg)