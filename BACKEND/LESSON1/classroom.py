# class Car:
#     brand="GM"
#     def __init__(self,year,price,color):
#         self.year=year
#         self.price=price
#         self.color=color

#     def __str__(self):
#         return f"{self.year}-yilgi mashina"
    
#     def __repr__(self):
#         return f"car(year={self.year},price={self.price})"
    
# obj1=Car(year=2025,price=10000,color="oq")
# obj2=Car(year=2022,price=8000,color="qizil")
# obj3=Car(year=2000,price=1000,color="qora")

# print(repr(obj1))
# print(obj2.year)
# print(obj2.price)
# print(obj2.color)

class Car:
    brand="GM"
    def __init__(self,year,price,color):
        self.year=year
        self.price=price
        self.color=color

    def __str__(self):
        return f"{self.year}-yilgi mashina"
    
    def __repr__(self):
        return f"car(year={self.year},price={self.price})"
    
    def star_Car(self):
        if not self.is_engine_on:
            self.is_engine_on=True
            
            return f"Car is successfully turned on!"
        return f"Car is already on you stupid!"
    
    def drive(self):
        if self.is_engine_on:
            return f"we are driving look at on your road!"
        return f"you should start engine on first!"
    
    def magnitafon(self):
        if self.working:
            return f"the tape is working!"
        return f"the cassete is not insert!"
    
gentra=Car(price=10000, color="qora", year=2023)
print(gentra.drive())
print(gentra.star_Car())
print(gentra.star_Car())
print(gentra.drive())
print(gentra.magnitafon())
