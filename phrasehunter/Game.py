import os
import time
import random


from phrasehunter.Phrase import Phrase


class Game():
    def __init__(self):
        self.missed = 0
        self.active_phrase = None
        self.used_phrases = []
        self.phrases = [
            "Were all going to die but not today",
            "Smooth like butter",
            "Light it up like dynamite",
            "You can do anything",
            "Love Myself"
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        
        
   def start(self):
         self.welcome()
         self.active_phrase = Phrase(self.get_random_phrase())
         while self.missed < 5:
               if not self.active_phrase.complete_check(self.guesses):
                  print("\nYou missed {} out of 5 misses.".format(self.missed))
                  self.active_phrase.display(self.guesses)
                  user_guess = self.get_guess()
                  self.guesses.append(user_guess)
                  if not self.active_phrase.check_letter(user_guess):
                    print("Oops! That letter is not in the phrase. {} out of 5 tries remaining!".format(4-self.missed))
                    self.missed += 1
                  if self.game_over():
                    break
                           
  
                                      
    def get_random_phrase(self):
        return random.choice(self.phrases)          
      

    def welcome(self):
        print (" ")
        print("******* WELCOME TO THE PHRASE HUNTER GAME!!! *******")
        print (" ")
        print("You'll get a random phrase from a list of {} phrases".format(len(self.phrases)))
        print("Guess individual letters in the phrase. You will win by guessing all the letters but lose if you miss five (5) guesses")
        print (" ")
        print("Ready? Okay, Let's goooooo!!!")
        print (" ")

    def get_guess(self):
        print(" ")
        while True:
            user_guess = input("Please guess a letter: ").lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                break
            else:
                print("Your guess has to be one (1) letter of the alphabet!")
        self.guesses.append(user_guess)
        return user_guess.lower

      
      
    def check_guess(self):
        return user_guess in self.active_phrase
      
      
    def game_over(self):
        if self.active_phrase.complete_check(self.guesses):
            print("Congrats!!!  ***** YOU WIN!!! ***** You guessed the phrase: {}".format(self.active_phrase.phrases))
            return True
        elif self.missed == 5:
            print("Oh no! You guessed incorrect 5 times. GAME OVER!!! The phrase was: {}".format(self.active_phrase.phrases))
            return True
        else:
            return False
