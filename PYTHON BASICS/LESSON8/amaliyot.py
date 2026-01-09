# otam={'ismi':'husan','t_yili':'1977','shahri':'qashqadaryo','manzili':'Dehqonobod'}
# print('otam haqida malumot')
# print(f'ismi:{otam['ismi']}')
# print(f't_yili:{otam['t_yili']}')
# print(f'shahri:{otam['shahri']}')
# print(f'manzili:{otam['manzili']}')

# ukam={}
# ukam['ismi']='mahmud'
# ukam['t_yili']='2012'
# ukam['shahri']='qashqadaryo'
# ukam['manzili']='dehqonobod'
# print(f'{ukam['ismi']}')
# print(f'{ukam['t_yili']}')
# print(f'{ukam['manzili']}')

# sevimli_taomlar={
#     'otam':'osh',
#     'onam':'manti',
#     'ukam':'somsa',
#     'singlim':'lavash',
#     'opam':'pitsa'
# }
# print(f'otamning sevimli taomi:{sevimli_taomlar['otam']}')
# print(f'ukamning sevimli taomi:{sevimli_taomlar['ukam']}')
# print(f'onamning sevimli taomi:{sevimli_taomlar['onam']}')

# python_suzlar={
# 'integer':'butun son',
# 'float':'unli kasr son',
# 'tuple':'uzgarmas ruyxat',
# 'string':'matn',
# 'if':'agar'
# }
# print(f'integer:{python_suzlar['integer']}')
# print(f'float:{python_suzlar['float']}')

# python_lugat={
#     'integer':'butun son',
#     'float':'unlik son',
#     'string':'matn',
#     'list':'ruyxat',
#     'tuple':'uzgarmas ruyxat',
#     'dictionary':'lugat'
# }
# for kalit in sorted(python_lugat):
#   qiymat=python_lugat[kalit]
#   print(f'{kalit.lower()}-{qiymat}')

# davlatlar_poytaxtlar={
#     'Uzbekiston':'Toshkent',
#     'Rossiya':'Moskva',
#     'AQSH':'Vashington',
#     'Germaniya':'Berlin',
#     'Yaponiya':'Tokio'
# }
# # print('davlatlar:')
# for davlatlar_poytaxtlar  in sorted(davlatlar_poytaxtlar.keys()):
#         print(davlat)
#         print('poytaxtlar:')
# for poytaxt in sorted(davlatlar_poytaxtlar.values()):
#         print(poytaxt)

# davlat=input('qaysi davlatning poytaxtini bilmoqchisiz?')
# poytaxt=davlatlar_poytaxtlar.get(davlat)
# if poytaxt:
#     print(f'{davlat}ning poytaxti {poytaxt}')
# else:
#     print(f'bizda bunday malumot yuq')

# menyu={
#         'osh':25000,
#         'shashlik':35000,
#         'lagmon':20000,
#         'manti':18000,
#         'non':5000,
#         'salat':10000
#     }
# buyurtmalar=[]
# print('3 ta taom buyurtma bering!')
# for n in range(3):
#         buyurtmalar.append(input(f'{n+1}-taom:').lower())
#         for buyurtma in buyurtmalar:
#             if buyurtma in menyu:
#                 print(f'{buyurtma.title()} {menyu[buyurtma]} sum')
#             else:
                # print(f'kechirasiz,bizda {buyurtma} yuq')
# shaxslar={
#      'ism':'Abu Abdullah Muhammad ibn Ismoil',
#      't_yil':810,
#      'shahar':'Buxoro',
#      'asarlar':['Al-jome as-sahih','Al-adab al-mufrad']
# },
# {
#      'ism':'Abdulla Qodiriy',
#      't_yil':1894,
#      'shahar':'Toshkent',
#      'asarlar':['utkan kunlar','mehrobdan chayon']
# },
# {
#      'ism':'Erkin Vohidov',
#      't_yil':1936,
#      'shahar':'Fargona',
#      'asarlar':['uzbegim','qiziquvchan matmusa']
# }
# for shaxs in shaxslar:
#      ism=shaxs['ism']
#      asarlar=shaxs['asarlar']
#      print(f'{ism}ning mashhur asarlari')
#      for asar in asarlar:
#           print(f'-{asar}')

# oila = {
#     'ali':['Terminator', 'Forsaj', 'Orgimchak odam'],
#     'vali': ['Mahallada duv-duv gap', 'Shum bola'],
#     'soli': ['Interstellar', 'Inception', 'Tenet']
# }

# for ism, kinolar in oila.items():
#     print(f"{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)

# davlatlar = {
#     "O'zbekiston": {
#         'poytaxt': 'Toshkent',
#         'maydon': 448.9,
#         'pul': "so'm"
#     },
#     "AQSH": {
#         'poytaxt': 'Vashington',
#         'maydon': 9.8,
#         'pul': 'dollar'
#     },
#     "Rossiya": {
#         'poytaxt': 'Moskva',
#         'maydon': 17.1,
#         'pul': 'rubl'
#     }
# }
# davlat = input("Davlat nomini kiriting: ")
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"{davlat}ning poytaxti {info['poytaxt']}. "
#           f"Maydoni: {info['maydon']} mln kv.km. "
#           f"Pul birligi: {info['pul']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q")

# son=float(input("Juft son kiriting!"))
# if son%2==0:
#    print("raxmat!")
# else:
#    print("bu son juft emas!")

# yosh=int(input('yoshingiz nechida?'))
# if yosh<=4 or yosh>=60:
#     narx=0
# elif yosh<18:
#     narx=10000
# else:
#     narx=20000
# print(f'Chipta {narx} sum')

# x=float(input("birinchi sonni kiriting:"))
# y=float(input("ikkinchi sonni kiriting:"))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar=['un','yog','tuxum','sovun','piyoz','kartoshka','banan','uzum','olma','qovun']
# savat=[]

# print("\nSavatga 5ta mahsulot kiriting:")
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qushing:").lower())

# for mahsulot in savat:
#      if mahsulot in mahsulotlar:
#          print(f"dukonimizda {mahsulot.title()} bor!")
#      else:
#          print(f"dukonimizda {mahsulot.title()} yuq")

# users=['alisher1983','yasina','aziza','umr']
# login=input('yangi login tanlang:')
# if login in users:
#     print('xush kelibsiz!')
# else:
#     print('login band,yangi login tanlang!')

# x=int(input('son kiriting!'))
# y=int(input('yana bir son kiriting!'))
# print(x,"/",y, "=", x/y)

