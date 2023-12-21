from blackjack_helper import *

# draw_starting_hand("YOUR") prints a turn message and assigns the starting hand value to user_hand_value.
user_hand_value = draw_starting_hand("YOUR") 

# The user has the option to keep drawing if their hand is below 21.
while user_hand_value < 21:
  should_hit = input('You have ' + str(user_hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
        user_hand_value += draw_card()
  else:
    print("Sorry I didn't get that.")

# User end turn status
print_end_turn_status(user_hand_value)

# The dealer starts to play. Prints Dealer Turn and assigns the value of initial hand to dealer_hand_value.
dealer_hand_value = draw_starting_hand("DEALER")
  

# The dealer has to keep drawing if their hand is below 17.
while dealer_hand_value < 17:
    print("Dealer has {}.".format(dealer_hand_value))
    dealer_hand_value += draw_card() 

# Dealer end turn Status
print_end_turn_status(dealer_hand_value)

# Game Result
print_end_game_status(user_hand_value, dealer_hand_value)




