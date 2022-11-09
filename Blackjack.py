############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
import os
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  # 11 is the Ace.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a List of cards as input and returns the score"""

  if sum(cards) == 21 and len(cards) == 2:
    return 21
  # Checking for an 11 (ace). If the score is already over 21, the Ace 11 will be removed and replaced with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score):
    """Compares the user and dealer scores to determine who has won and who has lost"""
    if user_score > 21 and dealer_score > 21:
        return "You went over. You both lost 😤"
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 21:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  dealer_cards = []
  is_game_over = False
  # Dealing 2 cards to each of the user and dealer using deal_card()
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  # Using a while loop so that the score and other checks in place can be rechecked with every new card drawn until the game ends.

  while not is_game_over:
    # Checking whether the dealer or the user have a blackjack (21) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   dealer's first card: {dealer_cards[0]}")

    if user_score == 21 or dealer_score == 21 or user_score > 21:
      is_game_over = True
    else:
      # If the game has not ended, ask the user if they want to draw another card.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Once the user is done, it's time to let the dealer play. The dealer should keep drawing cards as long as it has a score less than 17.
  while dealer_score != 21 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"dealer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()
