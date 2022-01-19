from random import choice
from game.cards import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        points (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.guess = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        card1 = Card()
        card1.show()
        print()
        print(f"The card is: {card1.value}")
        choice = input("Higer or lower? [h/l] ")
        card2 = Card()
        card2.show()
        print(f"Next card was: {card2.value}")
        if (card1.value > card2.value) and choice == "l":
            self.guess = True
        elif (card1.value < card2.value) and choice == "h":
            self.guess = True
        else:
            self.guess = False
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.guess:
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.score}")

        if self.score > 0:
            answer = input("Play again? [y/n] ")
            self.is_playing = (answer == "y")
        else:
            self.is_playing = False
       