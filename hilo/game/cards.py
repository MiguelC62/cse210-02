import random

class Card:
    """A set of 13 different cards and the director shows one at a time. 
    The player must guess if the new card is higher or lower than the 
    previous one.
   
    Attributes:
        value (int): The number of points.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def show(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
        
        #Sets the values of each number 1-11 to reflect a card suite,
        #for example, A for Ace(1), J for Jack(11), Q for Queen(12)
        #K for King(13)
        if self.value == 1:
            self.value = "A"
        elif self.value == 11:
            self.value = "J"
        elif self.value == 12:
            self.value = "Q"
        elif self.value == 13:
            self.value = "K"
        else:
            self.value = self.value
