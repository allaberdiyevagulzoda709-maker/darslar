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
