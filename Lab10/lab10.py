import cardsBasic

print("Welcome to War.")
junk = input("Press Enter to play.")

my_deck = cardsBasic.Deck()
my_deck.shuffle()
hand1_list=[]
hand2_list=[]
for i in range(5):
    hand1_list.append(my_deck.deal())
    hand2_list.append(my_deck.deal())

print("\nHand 1:", hand1_list)
print("Hand 2:", hand2_list)
print()

input1 = ""

while True:
    
    input1 = input("Keep going? (N/n to quit)")
    if input1 == "n":
        break
    if input1 == "N":
        break
    
    last_card_hand1 = hand1_list.pop(0)
    last_card_hand2 = hand2_list.pop(0)
    print("Hand1 threw down",last_card_hand1,", Hand2 threw down", last_card_hand2)
    if last_card_hand1.equal_rank(last_card_hand2):
        print(last_card_hand1, last_card_hand2, "of equal rank", "Tie")
        hand1_list.append(last_card_hand1)
        hand2_list.append(last_card_hand2)

    elif last_card_hand1.get_rank() == 1:
        print(last_card_hand1, "of higher rank than",last_card_hand2, " Hand1 wins.")
        hand1_list.append(last_card_hand1)
        hand1_list.append(last_card_hand2)

    elif last_card_hand2.get_rank() == 1:
        print(last_card_hand2, "of higher rank than",last_card_hand2, " Hand2 wins.")
        hand2_list.append(last_card_hand1)
        hand2_list.append(last_card_hand2)

    elif last_card_hand1.get_rank() > last_card_hand2.get_rank():
        print(last_card_hand1, "of higher rank than",last_card_hand2, " Hand1 wins.")
        hand1_list.append(last_card_hand2)
        hand1_list.append(last_card_hand1)

    else:
        print(last_card_hand2, "of higher rank than",last_card_hand1, " Hand2 wins.")
        hand2_list.append(last_card_hand2)
        hand2_list.append(last_card_hand1)


    print("")
    print("Hands are now:")
    print("Hand 1:",hand1_list)
    print("Hand 2:", hand2_list)

    if len(hand1_list) == 0:
        break
    if len(hand2_list) == 0:
        break

print()
if len(hand1_list) > len(hand2_list):
    print("Hand1 has more cards than Hand2, Hand1 wins.")
elif len(hand2_list) > len(hand1_list):
    print("Hand2 has more cards than Hand1, Hand2 wins.")
else:
    print("Cards in hand are equal, Tie.")

