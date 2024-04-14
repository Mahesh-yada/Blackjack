This project implements a simple simulator for the popular gambling card game, Blackjack. Blackjack is a game of skill and strategy where players aim to create a hand as close as possible to a sum of 21 without exceeding it. The simulator provides a platform to play Blackjack against a computerized dealer, following the standard rules of the game.

Features:

Gameplay Mechanics:

Players are dealt an initial hand of 2 cards.
Players can choose to "hit" (draw another card) or "stand" (keep their current hand).
Dealer plays according to fixed rules: stand on 17 or higher, hit otherwise.

Scoring System:

Face cards (Jacks, Queens, Kings) are worth 10 points each.
Aces are worth 11 points.
All other cards are worth their numerical value.

Outcomes:

Players can experience one of three outcomes: Win, Lose, or Push.
Win: Player has a hand value greater than the dealer without busting.
Lose: Player busts or has a hand value less than the dealer.
Push: Player's hand value matches that of the dealer.

Project Structure:

blackjack.py: Main script implementing the Blackjack game logic.

player.py: Class representing a player in the game.

deck.py: Class representing a deck of cards.

README.md: Documentation and usage instructions.

Usage:

Run blackjack.py.
Follow the prompts to play Blackjack against the computerized dealer.
Make choices to hit or stand based on your hand and the dealer's visible card.
The game will determine the outcome based on the rules and display the result.

Contributing:

Contributions, bug fixes, and suggestions are welcome.
Fork the repository, make your changes, and submit a pull request.

License:

This project is licensed under the MIT License.


If you'd prefer a video explanation of the game check one out here: https://www.youtube.com/watch?v=qd5oc9hLrXg
