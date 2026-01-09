# while True:
#     try:
#         x=int(input('son kiriting!'))
#         y=int(input('yana bir son kiriting!'))
#         print(x,"/",y, "=", x/y)
#         break
#     except ValueError:
#         print("faqat butun son kiriting!")
#     except ZeroDivisionError:
#         print("0 ga bulib bulmaydi! Qaytadan urining")

# sonlar=[1,4,3,9,6,4]
# print("elemantlar soni:",len(sonlar))
# print("Eng katta qiymat:",max(sonlar))
# print("Eng kichik qiymat:",min(sonlar))
# print("Yigindini hisoblash:",sum(sonlar))

def son_uzunligi(son):
    return len(str(son))
print(son_uzunligi(139876543))

def sonning_kattasi(num1,num2,num3,num4):
    return max(num1,num2,num3,num4)
print(sonning_kattasi(1,3,6,7))

def sonning_kichigi(a,b,c,d):
    return min(a,b,c,d)
print(sonning_kichigi(78,45,34,89))

def yigindi_hisoblash(a,b,c,d,e):
    return sum(a,b,c,d,e)
print(yigindi_hisoblash(5,6,3,8,4))