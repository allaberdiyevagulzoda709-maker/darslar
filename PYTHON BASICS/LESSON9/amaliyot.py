# def salom_beruvchi():
#     return "Assalomu aleykum"
# print(salom_beruvchi())

# def opamning_ismi(ism="Farangiz"):
#     return f"Mening opamning ismi-{ism} "
# print(opamning_ismi())

# def katta_kichikni_topish(num1,num2,):
#     if num1>=num2:
#         return num1
#     return num2
# print(katta_kichikni_topish(num1=89,num2=6))

# def salom_ber(ism="hasan"):
#     return f"Assalomu alekum {ism}"
# print(salom_ber())

# def tugilgan_yil():
#     ism=input("ismingizni kiriting:")
#     yosh=int(input("yoshingizni kiriting:"))
#     yil=2025-yosh
#     print(f"{ism}, siz {yil}-yilda tugilgansiz")

# def tugilgan_yil(ism,yosh):
#     yil=2025-yosh
#     return f"{ism}, siz {yil}-yilda tugilgansiz"
# natija=tugilgan_yil("gulzoda",20)
# print(natija)

# def kvadrat_kub(son):
#     return son**2, son**3
# kvadrat_kub=kvadrat_kub(3)
# print(kvadrat_kub)

# def juft_toq(son):
#     if son%2==0:
#         return "Juft son"
#     return "Toq son"
# print(juft_toq(6))

# def sonlar(son1,son2):
#     if son1==son2:
#         return "sonlar teng"
#     return "teng emas"
# print(sonlar(2,2))

# def daraja(x,y=4):
    # return x**y
# print(daraja(5,3))

# def bulinishlar(son):
#     natija=[]
#     for i in range(2,11):
#         if son%i==0:
#             natija.append(i)
#     return natija
# print(bulinishlar(10))

    
def kvadrat_kub(son1,son2):
    son=int(input( son1=4,son2=7))
    print("kvadrat",son**2)
    print("kub",son**3)
