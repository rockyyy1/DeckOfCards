# DeckOfCards



Card class : repr

Class representing a playing card

DeckOfCards class: creates a 52 card deck of playing cards with methods to shuffle, deal and display deck 

Player(DeckOfCards) class: inherits the DeckOfCards class and has a method to simulate a game of snap in terminal.

To play game of snap:
play = Player()
play.snap(integer) with the integer being the number of players 

The simulation will deal an equal number of cards to the players. E.g 4 players:
![image](https://github.com/rockyyy1/DeckOfCards/assets/124854700/791e0efd-8fc5-48e4-98a5-d775eee2eb0e)

Each turn, a player will flip over the first card in their hand and place it into the central pile.

If a player places a card that is identicial to the top card of the central pile:

A random player will yell "SNAP" and collect all the cards in the central pile into their own hand.
![image](https://github.com/rockyyy1/DeckOfCards/assets/124854700/2b6c34f5-1781-48d0-a51c-4c6246f66df5)

The game ends when a player places down their last card and the player with the most cards wins. 
![image](https://github.com/rockyyy1/DeckOfCards/assets/124854700/a9942283-707b-4abe-8616-495bf1b6adac)
