  ##################################################################
  #  Section 001H
  #  Computer Project #2
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################
print("Your mission, should you choose to accept it, is to find a six-digit")
print("number 'SLAYER' that satisfies the following equation")
print("P.S. Each letter stands for the digit in the position shown:")
print("")
print("SLAYER + SLAYER + SLAYER = LAYERS")
#This just prints the challenge to the user.

slayer_int = int(input("My guess for SLAYER is: "))
slayer_ones = int(slayer_int%10)
slayer_tens = int((slayer_int//10)%10)
slayer_hund = int((slayer_int//100)%10)
slayer_thou = int((slayer_int//1000)%10)
slayer_tenthou = int((slayer_int//10000)%10)
slayer_hundthou = int((slayer_int//100000)%10)
#this splits up the inputted number into the individual digits

layers = int(slayer_hundthou + (slayer_ones*10) + (slayer_tens*100) +
             (slayer_hund*1000) + (slayer_thou * 10000) +
             (slayer_tenthou * 100000))
slayer3_int = int(slayer_int * 3)
#now we have defined LAYERS for later use. Also, slayer3_int will be a useful
#shortcut in the future.

if (slayer_int//100000) >= 10 or -10 < (slayer_int//100000) <=0 or (slayer_int//100000) < -10:
    print("Your guess is incorrect.")
    print("SLAYER must contain 6 non-zero digits and it must be positive.")
    print("You have failed your mission.")
#this statement checks to see if we have exactly 6 digits in the user's guess
#also, it checks to make sure that SLAYER is a positive number
    
elif (slayer3_int) != layers:
    print("Your guess is incorrect.")
    print("SLAYER + SLAYER + SLAYER = ", slayer3_int)
    print("LAYERS = ", layers)
    print("You have failed your mission.")
#this statement checks to see if SLAYER * 3 is equal to LAYERS
#if it is not, a message telling the user they have failed prints
    
else:
    print("Your guess is correct.")
    print("SLAYER + SLAYER + SLAYER = ", slayer3_int)
    print("LAYERS = ", layers)
    print("Your mission was a success.")
#this statement only runs if SLAYER * 3 = LAYERS and SLAYER is 6 digits












