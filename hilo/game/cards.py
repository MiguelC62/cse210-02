import random

class Card:
    """A set of 13 different cards and the director shows one at a time. 
    The player must guess if the new card is higher or lower than the 
    previous one. The player has three tries to be wrong.
   
    Attributes:
        value (int): The number of points.
        string_value (string): The suite card value as string
    """

    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.string_value = ""

    def show(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)

    def suite_card(self):
        """"
        Sets the values of each number 1-13 to reflect a card suite,
        for example, A for Ace(1), J for Jack(11), Q for Queen(12), and K for King(13)
        """
        if self.value == 1:
            self.string_value = "A"
        elif self.value == 11:
            self.string_value = "J"
        elif self.value == 12:
            self.string_value = "Q"
        elif self.value == 13:
            self.string_value = "K"
        else:
            self.string_value = str(self.value)
    
