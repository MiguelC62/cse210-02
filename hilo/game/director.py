from game.cards import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        guess (boolean): If the gamer guesses correctly
        lives (int): The lives's game for wrong guess
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.guess = True
        self.lives = 3

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing and self.lives > 0:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if card is high or low.

        Args:
            self (Director): An instance of Director.
        """
        #lives = 3
    #while self.lives > 0:
        card1 = Card()
        card1.show()
        print()
        print(f"The card is: {card1.value}")
        choice = input("Higer or lower? [h/l] ")
        card2 = Card()
        card2.show()
        print(f"Next card was: {card2.value}")
    
        #Error handling for TypeError (int and str)
        
        try:
            if (card1.value > card2.value) and choice == "l":
                self.guess = True
                #break
            elif (card1.value < card2.value) and choice == "h":
                self.guess = True
                #break
            else:
                self.guess = False
                self.lives -= 1
                print(f"You are left with {self.lives} tries.")
                if self.lives == 0:
                    #self.is_playing = False
                    print("Game Over")
                #else:
                    # self.guess = False
                    #break
        except TypeError as err:
            pass
       
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
        """Displays the cards and the score. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return

        #if self.score > 0 and self.lives == 0:
        if self.lives == 0:
            print(f"Your final score was: {self.score}")
            answer = input("Play again? [y/n] ")
            self.is_playing = (answer == "y")
            self.lives = 3
        elif self.score > 0:
            print(f"Your score is: {self.score}")
            self.is_playing = True
        else:
            self.is_playing = False