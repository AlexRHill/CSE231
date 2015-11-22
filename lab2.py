import math
import winsound
#these will allow us to accomplish later tasks

octpch1 = float(input("Gimme tha first octpch pair: "))
octpch2 = float(input("I want another octpch pair: "))
octpch3 = float(input("1 MORE OCTPCH PAIR PLS: "))

#now we will set some numbers aside for later conversion
number1 = octpch1//1
decimal1 = round((octpch1 % 1) * 10)
    
number2 = octpch2//1
decimal2 = round((octpch2 % 1) * 10)
    
number3 = octpch3//1
decimal3 = round((octpch3 % 1) * 10)

#now we convert these given values to Hertz 
expo1 = math.pow(2,(number1 + decimal1/12))
hertz1 = 16.35159 * expo1

expo2 = math.pow(2,(number2 + decimal2/12))
hertz2 = 16.35159 * expo2

expo3 = math.pow(2,(number3 + decimal3/12))
hertz3 = 16.35159 * expo3


#we now check for our 3 errors
if octpch1 < 0 or octpch2 < 0 or octpch3 < 0:
    print("NO NEGATIVE OCTPCH VALUES! Try again.")

elif decimal1 > 12 or decimal2 > 12 or decimal3 > 12:
    print("Semitone value must be between 0 and 12. Try again.")

elif hertz1 < 32 or hertz1 > 32676 or hertz2 < 32 or hertz2 > 32676 or hertz3 < 32 or hertz3 > 32676:
    print("One of your Hertz values do not fall in proper range of 32 to 32676. Try again.")
else:
    




    print("The first octpch pair is", octpch1)
    print("The second octpch pair is", octpch2)
    print("The third octpch pair is", octpch3)
    print("The first octpch pair converted to Hertz is", hertz1)
    print("The second octpch pair converted to Hertz is", hertz2)
    print("The third octpch pair converted to Hertz is", hertz3)

soundq = str(input("Do you want to hear these frequencies as sounds? "))

if soundq == "Yes" or "yes":
    hertz1int = int(round(hertz1))
    hertz2int = int(round(hertz2))
    hertz3int = int(round(hertz3))
    winsound.Beep(hertz1int, 500)
    winsound.Beep(hertz2int, 500)
    winsound.Beep(hertz3int, 500)
else:
    print("Goodbye.")

