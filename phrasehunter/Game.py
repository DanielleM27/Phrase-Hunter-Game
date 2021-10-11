import random
import time


from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.active_phrase = None
        self.missed = 0
        self.phrases = [
            "We're all going to die but not today",
            "If life wants to be funny i'll treat it like a joke",
            "Don't worry Be happy",
            "You can do anything",
            "Love Myself"
        ]
        self.guesses = []
        
        

    def start(self):
        self.welcome()
        play_game = True
        while play_game:
            self.active_phrase = Phrase(self.get_random_phrase())
            while self.missed < 5:
                if not self.active_phrase.complete_check():
                    self.active_phrase.display()
                    user_guess = self.get_guess()
                    if self.active_phrase.letter_check(user_guess):
                        print("Great! {} is in the phrase".format(user_guess))
                    else:
                        print("Oops! {} is not in the phrase. {} out of 5 lives remaining!".format(user_guess, 4-self.missed))
                        self.missed += 1
                    print()
                else:
                    break
            play_game = self.game_over()
            
            
            
            

    def get_random_phrase(self):
        return random.choice(self.phrases)    
      
      
      

    def welcome(self):
        print("└[∵┌]└[ ∵ ]")
        print("Welcome to the best Phrase Hunter Game!!!")
        time.sleep(0.5)
        print("You'll get a random phrase from a list of {}".format(len(self.phrases)))
        time.sleep(0.5)
        print("Guess individual letters in the phrase")
        time.sleep(0.5)
        print("Ready? Okay, Let's goooooo!!!")
        time.sleep(1)
        
        
        

    def get_guess(self):
        while True:
            user_guess = (input("Please can you guess a letter: ")).lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                break
            else:
                print("Please make sure your guess is 1 letter!")
        self.guesses.append(user_guess)
        return user_guess
      
      
      

    def game_over(self):
        if self.missed < 5:
            print("Congrats!!! You guessed the phrase: {}".format(self.active_phrase.phrase))
        else:
            print("Ooops! You guessed incorrect 5 times. Game over!!!")
            print("The phrase was: {}".format(self.active_phrase.phrase))
            print("\nThank you so much for playing. See you next time!!!")      
        
            return False