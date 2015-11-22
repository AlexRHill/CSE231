  ##################################################################
  #  Section 001H
  #  Computer Project #3
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################

nickels_int = 25
dimes_int = 25
quarters_int = 25
ones_int = 0
fives_int = 0

print("Welcome to tha ghetto vending machine.")

#I took some creative liberties with my naming conventions to allow myself to have more fun as I made the program

while True:

#and here we start the loop that will go on for the whole program

    total_int = (nickels_int * 5) + (dimes_int * 10) + (quarters_int * 25) + (ones_int * 100) + (fives_int * 500)
    nickels_change = 0
    dimes_change = 0
    quarters_change = 0
    deposit_int = 0
    dollars_int = 0

#resetting these values is key to making this work
    
    print(" ")
    print("Stock contains:")
    print("   ",nickels_int,"nickels")
    print("   ",dimes_int,"dimes") 
    print("   ",quarters_int,"quarters")
    print("   ",ones_int,"one dolla bills")
    print("   ",fives_int,"five dolla bills")

    print(" ")
    price = input("How much is yo item foo? Enter like (xx.xx) or hit q to quit dawg: ")

    if price != 'q':
        price_float = float(price)
    else:
        print(" ")
        print("Have a good day homie.")
        if ((total_int-(total_int%100))//100) != 0:
            print("Total:",((total_int-(total_int%100))//100),"dolla and",total_int%100,"cents.")
        else:
            print("Total:",total_int%100,"cents.")
            
        break

    #we check to see what the user inputs. if q, we add up the total amount in the machine and end the loop/program

    if ((round(price_float*100))/5)%1 != 0:
        print("Item price must be a multiple of 5 cents homie. Try again.")
        continue 
    
    print("Menu for deposits:")
    print("  'n' - deposit yo nickel")
    print("  'd' - deposit yo dime")
    print("  'q' - deposit yo quarter")
    print("  'o' - deposit yo one dolla bill")
    print("  'f' - deposit yo five dolla bill")
    print("  'c' - cancel yo purchase dawg")

    price_int = int(price_float)
    dollars_int = int(price_int//1)
    cents_int = int(round((price_float - dollars_int) * 100))

    #these variables are crucial to the calculations done from here out
    
    while dollars_int > 0 or cents_int > 0:
        
        if cents_int < 0 and dollars_int >= 1:
            dollars_int -= 1
            cents_int += 100            
          
               
        print("")
        print("Payment due:", dollars_int, "dollars and",cents_int,"cents.")
        deposit = input("What you depositing dawg? ")
        
        
        if deposit == "n":
            cents_int -= 5
            deposit_int += 5
            nickels_int += 1

            #for each coin/dollar input, we subtract the corresponding amount from the price of the item, add to a variable we will use if the user decides
            #to cancel their purchase, and add the coin inputted to the variable that keeps track of the stock
            
        elif deposit == "d":
            cents_int -= 10
            deposit_int += 10
            dimes_int += 1
            
        elif deposit == "q":
            cents_int -= 25
            deposit_int += 25
            quarters_int += 1
            
        elif deposit == "o":
            dollars_int -= 1
            deposit_int += 100
            ones_int += 1
            
        elif deposit == "f":
            dollars_int -= 5
            deposit_int += 500
            fives_int += 1
            
        elif deposit == "c":
            
            if deposit_int > 0:
                print(" ")
                print("Take yo change below.")
            
                while deposit_int > 0:
                    #here we begin the complicated process of checking the best way to give out change. every possibility is accounted for and the way where
                    #the user receives the least amount of coins is what is done
                    if deposit_int / 25 >= 1:
                        if quarters_int >= 1:
                            quarters_int -= 1
                            deposit_int -= 25
                            quarters_change += 1
                        elif deposit_int / 10 >= 1 and quarters_int == 0 and dimes_int >= 1:
                            dimes_int -= 1
                            deposit_int -= 10
                            dimes_change += 1
                        elif quarters_int == 0 and dimes_int >= 2 and nickels_int >= 1:
                            dimes_int -= 2
                            nickels_int -= 1
                            deposit_int -= 25
                            dimes_change += 2
                            nickels_change += 1
                        elif quarters_int == 0 and dimes_int <= 1 and nickels_int >= 5:
                            nickels_int -= 5
                            deposit_int -= 25
                            nickels_change += 5
                        elif quarters_int == 0 and nickels_int <= 5 and dimes_int >= 2:
                            dimes_int -= 2
                            deposit_int -= 20
                            dimes_change += 2
                            break
                        elif quarters_int == 0 and dimes_int == 0 and nickels_int >= 1:
                            nickels_int -= 1
                            deposit_int -= 5
                            nickels_change += 1
                        elif quarters_int == 0 and nickels_int == 0 and dimes_int == 0:
                            break
                    elif deposit_int / 10 >= 1:
                        if dimes_int >= 1:
                            dimes_int -= 1
                            deposit_int -= 10
                            dimes_change += 1
                        elif dimes_int == 0 and nickels_int >= 2:
                            nickels_int -= 2
                            deposit_int -= 10
                            nickels_change += 2
                        elif quarters_int == 0 and nickels_int == 0 and dimes_int == 0:
                            break
                    elif deposit_int / 5 >= 1:
                        if nickels_int >= 1:
                            nickels_int -= 1
                            deposit_int -= 5
                            nickels_change += 1
                    elif quarters_int == 0 and nickels_int == 0 and dimes_int == 0:
                        break
                
                if nickels_change > 0:
                    print(nickels_change, "nickels")
                if dimes_change > 0:
                    print(dimes_change, "dimes")
                if quarters_change > 0:
                    print(quarters_change, "quarters")
                    #here we print out if the user received change only if there was change in that denomination

            if deposit_int != 0:
                print(" ")
                print("Da machine is outta change.")
                print("See da store manager for yo refunds doe.")
                if ((deposit_int-(deposit_int%100))//100) != 0:
                    print("Amount due:",((deposit_int-(deposit_int%100))//100),"dolla and",deposit_int%100,"cents.")
                else:
                    print("Amount due:",deposit_int%100,"cents.")
                    #if not enough change is contained in the machine to give out change, then we tell the user how much is owed to them
            
            break

        else:
            print("Illegal selection:",deposit)
            #if the input is not one contained in the deposits menu, the user is told the selection is illegal and then is able to try again

        if dollars_int < 0: 
            cents_int += (dollars_int * 100)
            dollars_int = 0

        

    else:
         
        if dollars_int < 0:
            cents_int = cents_int + (dollars_int * 100)
            dollars_int = 0
            
        cents_int = cents_int * -1
        if cents_int > 0:
            print(" ")
            print("Take yo change below.")
            
            while cents_int > 0:
                #the same change mechanism as above is implemented
               if cents_int / 25 >= 1:
                   if quarters_int >= 1:
                       quarters_int -= 1
                       cents_int -= 25
                       quarters_change += 1
                   elif cents_int / 10 >= 1 and quarters_int == 0 and dimes_int >= 1:
                       dimes_int -= 1
                       cents_int -= 10
                       dimes_change += 1
                   elif quarters_int == 0 and dimes_int >= 2 and nickels_int >= 1:
                       dimes_int -= 2
                       nickels_int -= 1
                       cents_int -= 25
                       dimes_change += 2
                       nickels_change += 1
                   elif quarters_int == 0 and dimes_int <= 1 and nickels_int >= 5:
                       nickels_int -= 5
                       cents_int -= 25
                       nickels_change += 5
                   elif quarters_int == 0 and nickels_int <= 5 and dimes_int >= 2:
                       dimes_int -= 2
                       cents_int -= 20
                       dimes_change += 2
                       break
                   elif quarters_int == 0 and dimes_int == 0 and nickels_int >= 1:
                       nickels_int -= 1
                       cents_int -= 5
                       nickels_change += 1
                   elif quarters_int == 0 and nickels_int == 0 and dimes_int == 0:
                       break
               elif cents_int / 10 >= 1:
                   if dimes_int >= 1:
                        dimes_int -= 1
                        cents_int -= 10
                        dimes_change += 1
                   elif dimes_int == 0 and nickels_int >= 2:
                        nickels_int -= 2
                        cents_int -= 10
                        nickels_change += 2
                   elif dimes_int == 0 and nickels_int == 1:
                        nickels_int -= 1
                        cents_int -= 5
                        nickels_change += 1
                        break
                   elif nickels_int == 0 and dimes_int == 0:
                       break
               elif cents_int / 5 >= 1:
                   if nickels_int >= 1:
                        nickels_int -= 1
                        cents_int -= 5
                        nickels_change += 1
                   elif nickels_int == 0:
                       break
                    
        if nickels_change > 0:
            print(nickels_change, "nickels")
        if dimes_change > 0:
            print(dimes_change, "dimes")
        if quarters_change > 0:
            print(quarters_change, "quarters")
        if nickels_change == 0 and dimes_change == 0 and quarters_change == 0 and cents_int == 0:
            print(" ")
            print("Take yo change below.")
            print("No change.")
            
        if cents_int != 0:
            print(" ")
            print("Da machine is outta change.")
            print("See da store manager for yo refunds doe.")
            if ((cents_int-(cents_int%100))//100) != 0:
                print("Amount due:",((cents_int-(cents_int%100))//100),"dolla and",cents_int%100,"cents.")
            else:
                print("Amount due:",cents_int%100,"cents.")
  
     
