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
        None

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
            for i in range(cards_per_player):
                random_index = random.randrange(len(self.cards))
                card = self.cards.pop(random_index)
                player_hand.append(card)
                
        player_number = 1
        for player_hand in hands:
            print(f"Player {player_number}:", player_hand)
            player_number += 1
        print()        
        return(hands)

class Player(DeckOfCards):
    def __init__(self):
        DeckOfCards.__init__(self)
        
    def snap(self, number_of_players):
        central_pile = []
        play = self.deal(number_of_players)
        player = 1
        for i in play:
            print(f"Player {player} turns over a", i[0])
            #remove from players hand and into central pile
            central_pile.append(i[0])
            i.pop(0)
            #check to see if the central pile's top two cards are identical
            if len(central_pile) > 1:
                if central_pile[-1].value == central_pile[-2].value:
                    print(f"\nPLAYER {player} YELLS SNAP\n")
                    #put all the central pile into player's hand
                    for cards in range(len(central_pile)):
                        i.append(central_pile.pop(-1))
            if len(i) == 0:
                print("Player {player} has run out of cards. game over")
                break
            player += 1
            
        print("\nCentral pile:", central_pile)
        print()
        player_count = 1
        for i in play:
            print(f"Player {player_count}:", i)
            player_count += 1

def main():
    # deck.shuffle()
    # deck.display_deck()
    # deck = DeckOfCards()
    play = Player()
    play.snap(4)

if __name__ == "__main__":
    main()
