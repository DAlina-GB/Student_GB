# фунция которая переводит мили в коллометры

# def Converts(miles):
#     km = miles * 1.609
#     print (km)
    
# miles = int (input ("Input miles "))
# print = Converts (miles)


# def Converts(miles):
#     return miles * 1.609
# km = float(input(f"Введите расстояние в милях:  "))
# print (f"{Converts(km), 'kilometers'}")

# Расчет площади прямоугольника
# a = 3
# b = 4
# def Area(a,b):
#     return a * b

# a = int(input("enter the length "))
# b = int(input("enter the width "))
# sq = Area(a,b)
# print ("Площадь прямоугольника - " + str(sq))

# определить четное число или нет
def Is_even(a):
    b = a % 2
    if b == 0:
        return "even"
    else: 
        return "not even"

a = int(input("unput numbers  "))
print (Is_even(a))
