import os
import time
import random


from phrasehunter import Phrase


phrases = [
            "We're all going to die but not today",
            "If life wants to be funny i'll treat it like a joke",
            "Don't worry Be happy",
            "You can do anything",
            "Love Myself"
          ]


class Game():
    def __init__(self):
        self.missed = 0
        self.active_phrase = None
        self.guesses =[]       
        
        
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
                    play_game = self.game_over()            
            

    def get_random_phrase(self):
        return random.choice(self.phrases)          
      

    def welcome(self):
        print("Welcome to Phrase Hunter Game!!!")
        print("You'll get a random phrase from a list of {}".format(len(self.phrases)))
        print("Guess individual letters in the phrase. You win by guessing all the letters but lose if you miss five (5) guesses")
        print("Ready? Okay, Let's goooooo!!!")
        

    def get_guess(self):
        while True:
            user_guess = input("Guess a letter: ").lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                break
            else:
                print("Your guess has to be 1 letter!")
        self.guesses.append(user_guess)
        return user_guess.lower
      
      
    def game_over(self):
        if self.missed < 5:
            print("Congrats!!! You guessed the phrase: {}".format(self.active_phrase.phrase))
        else:
            print("Ooops! You guessed incorrect 5 times. Game over!!!")
            print("The phrase was: {}".format(self.active_phrase.phrase))    
        return False