#Semester Project: Blackjack Game

import random

#Deck of cards
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

#Shuffle Deck
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

#Calculate hand value
def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

#Display hand
def display_hand(hand, hide_first_card = False):
    if hide_first_card:
        return "[Hidden], " + ", ".join(f"{rank} of {suit}" for rank, suit in hand[1:])
    else:
        return ", ".join(f"{rank} of {suit}" for rank, suit in hand)

#Main game
def play_blackjack():
    deck = create_deck()
   
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
   
    print("\n === Welcome to Blackjack! ===")
    print(f"Dealer's Hand: {display_hand(dealer_hand, hide_first_card = True)}")
    print(f"Your Hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
   
#Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)

        if player_value == 21:
            print("Blackjack. You win!")
            return

        if player_value > 21:
            print("Bust. Dealer wins!")
            return
        choice = input("Do you want to Hit (H) or Stand (S)? ").strip().lower()

        if choice == 'h':
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f"\nYou drew: {new_card[0]} of {new_card[1]}")
            print(f"Your Hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")

        elif choice == 's':
            break

        else:
            print("Invalid input. Please enter H or S.")

#Dealer's turn
    print("\n=== Dealer's Turn ===")
    print(f"Dealer's Hand: {display_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    while calculate_hand_value(dealer_hand) < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print(f"Dealer draws: {new_card[0]} of {new_card[1]}")
        print(f"Dealer's Hand: {display_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    # Final results
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print("\n=== Final Results ===")
    print(f"Your Hand: {display_hand(player_hand)} (Value: {player_value})")
    print(f"Dealer's Hand: {display_hand(dealer_hand)} (Value: {dealer_value})")

    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
       
#Run game
while True:
    play_blackjack()
    replay = input("\nPlay again? (Y/N): ").strip().lower()
    if replay != 'y':
        print("Thanks for playing!")
        break