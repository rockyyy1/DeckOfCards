import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        """Using the Card class, create list of 52 cards, 13 (2-A) from each suit (Hearts, Diamonds, Spades, Clubs)
        
        Args:
        valueList (list): A list of 13 strings, one for each card value (2-A).
        suitList (list): A list of 4 strings, one for each card suit (Hearts, Diamonds, Spades, Clubs).

        Returns:
        cards (list): A list of 52 Card objects.
        """
        valueList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suitList = ["Hearts", "Diamonds", "Spades", "Clubs"]    
        self.cards = []
        for suit in suitList:
            for value in valueList:
                card = Card(value, suit)
                self.cards.append(card)

    def display_deck(self):
        """Prints a list of cards
        
        Args: 
        cards (list) - list of cards
        
        Returns:
        None
        """
        for card in self.cards:
            print(card)
        
    def shuffle(self):
        """Shuffles list of cards randomly
        
        Args:
        cards (list) - list of cards to shuffle
        
        Returns:
        None
        """
        random.shuffle(self.cards)

    def deal(self, players):
        """Randomly distrubutes cards equally to given number of players
        
        Args:
        players (int) - the number of players
        
        Returns:
        hands (list) - list of cards given to each player
        """
        #create the number of players' hands
        hands = []
        for i in range(players):
            hands.append([])
            
        #how many cards each player should receive, ignoring the remainder
        cards_per_player = len(self.cards) // players
        
        #distribute equal number of cards to each player
        for player_hand in hands:
            for _ in range(cards_per_player):
                random_index = random.randrange(len(self.cards))
                card = self.cards.pop(random_index)
                player_hand.append(card)
                
        player_number = 1
        for player_hand in hands:
            print(f"Player {player_number}:")
            for card in player_hand:
                print(card, end = "\n")
            player_number += 1
            print()


class Player(DeckOfCards):
    def show_first_card(self):
        for hand in self.hands:
            print(hand[0])

         
def main():
    # deck.shuffle()
    # deck.deal(4)
    # deck.display_deck()
    deck = DeckOfCards()
    deck.deal(4)
    player = Player(deck)
    player.show_first_card()
    

if __name__ == "__main__":
    main()
