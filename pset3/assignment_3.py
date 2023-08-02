import random
import requests

"""

Question 1

"""

class Card():
    
    def __init__(self, suit, rank):
        #Define attributes of class
        self.rank = rank
        self.suit = suit
        if self.rank == 'Two':
            self.points = 2
        elif self.rank == 'Three':
            self.points = 3
        elif self.rank == 'Four':
            self.points = 4
        elif self.rank == 'Five':
            self.points = 5
        elif self.rank == 'Six':
            self.points = 6
        elif self.rank == 'Seven':
            self.points = 7
        elif self.rank == 'Eight':
            self.points = 8
        elif self.rank == 'Nine':
            self.points = 9
        elif self.rank == 'Ten' or self.rank == 'Jack' or self.rank == 'Queen' or self.rank =='King':
            self.points = 10
        elif self.rank == 'Ace':
            self.points = 11
        
    def __str__(self):
        # Defien method for printing object in class
        return self.rank + " of " + self.suit + " - " + str(self.points) 

class Deck():
    
    def __init__(self):
        """
        Use loops to create a list of 52 cards
        """
        
        # Establish ranks and suits
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

        hand = []

        # Create a list of cards of class Card
        for suit in suits:
            for rank in ranks:
                hand.append(Card(suit, rank))
        
        # Shuffle deck
        random.shuffle(hand)
        
        # Define list as items attribute
        self.items = hand
        
    def pop_card(self):
        # If list(deck) not empty
        if self.items:
            # Choose random card
            card = random.choice(self.items)
            # Remove it drom deck
            self.items.remove(card)
            # Return it
            return card
        # If deck empty -> return None
        else:
            return None   
        
        
         
    
"""

Question 2

"""


def station_bikes(station_name):
    # Get API from URL
    url = "https://api.citybik.es/v2/networks/gira?fields=stations"

    response = requests.get(url)

    # Data sorting
    data = response.json()
    stations = data['network']['stations']

    main = []

    # Iterate over list of stations
    for dicto in stations:
        # Create an empty temporary dictonart
        temp = {}
        # Extract empty slots, free bikes and name and insert into temporary dict
        temp['empty_slots'] = dicto['empty_slots']
        temp['free_bikes'] = dicto['free_bikes']
        temp['name'] = dicto['name']
        # Append temporary dict to main list
        main.append(temp)
        
    # Iterate over sations again
    for dicto in main:
        # Remove numbers, spaces and dash from station name
        dicto['name'] = dicto['name'][6:]
    
    # Iterate over stations again
    for dicto in main:
        # If station name found
        if station_name in dicto['name']:
            # Return Capacity
            return(dicto['empty_slots'] + dicto['free_bikes'])
    # If station name not found - raise NameError
    raise NameError("Station not found")



"""
Test your functions here
You must comment your tests when submiting your work
"""

# Question 1

card = Card("Spades", "Four")
print(card.points) #4
print(card) #Four of Spades - 4

deck1 = Deck()
print(deck1.pop_card()) #Jack of Hearts - 10
print(deck1.pop_card()) #Queen of Spades - 10

deck2 = Deck()
print(deck2.pop_card()) #Six of Spades - 6


# Question 2
print("-"*16)

print(station_bikes("Gare do Oriente")) #40
print(station_bikes("Av. Paris / Av. Almirante Reis")) #14

