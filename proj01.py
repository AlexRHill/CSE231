richter = input("Enter a Richter Scale Measure: ")
richter_float = float(richter)

joule = float(10**((1.5*richter_float)+4.8))

TNT = float(joule/4.184e9)

print("Richter measure:",richter)
print("Equivalence in Joules:",joule)
print("Equivalence in Tons of TNT:",TNT)

print(" ")
print("Richter  Joules                 TNT")

rich = 10**((1.5*1)+4.8)
poor = 10**((1.5*1)+4.8)/4.184e9
print("1       ",rich,"   ",poor)

bleh = 10**((1.5*5)+4.8)
blah = 10**((1.5*5)+4.8)/4.184e9
print("5       ",bleh,"   ",blah)

meh = 10**((1.5*9.1)+4.8)
mah = 10**((1.5*9.1)+4.8)/4.184e9
print("9.1     ",meh,"",mah)

taco = 10**((1.5*9.2)+4.8)
burrito = 10**((1.5*9.2)+4.8)/4.184e9
print("9.2     ",taco,"",burrito)

car = 10**((1.5*9.5)+4.8)
caravan = 10**((1.5*9.5)+4.8)/4.184e9
print("9.5     ",car,caravan)
