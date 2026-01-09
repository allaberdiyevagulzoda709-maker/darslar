# def davlatlar_poytaxtlar():
#     return{
#     'Uzbekiston':'Toshkent',
#     'Rossiya':'Moskva',
#     'AQSH':'Vashington',
#     'Germaniya':'Berlin',
#     'Yaponiya':'Tokio'
#     }
# for davlatlar_poytaxtlar  in sorted(davlatlar_poytaxtlar().values()):
#         print(davlatlar_poytaxtlar.title())

# def func_nomi(t_yil,h_yil):
#       yosh=h_yil - t_yil
#       v_yetgan=False
#       if yosh>=18:
#             v_yetgan=True
#       return dict(yosh=yosh,voyaga_yetgan=v_yetgan)
# print(func_nomi(t_yil=2009,h_yil=2026))
# print(func_nomi(t_yil=2003,h_yil=2025))
# print(func_nomi(t_yil=2005,h_yil=2023))

# def salom_beruvchi(ism):
#     return f"assalomu alekum: {ism}"
# print(salom_beruvchi(ism="vali"))
# print(salom_beruvchi(ism="oysha"))

# def katta_kichik(num1,num2):
#     if num1>=num2:
#         return num1
#     return num2
# print(katta_kichik(num1=3, num2=5))

list=[1,2,56,76,23,45,59]
def custom_max(a):
    if not a:
        return "list bush"
    max_num=a[0]
    for num in a:
        if num>max_num:
            max_num=num
            return max_num
        print(custom_max())