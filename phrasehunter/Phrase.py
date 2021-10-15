class Phrase:

  
  def __init__(self, phrase):
        self.phrase = phrase.lower()
      
        self.phrase_list = []
        self.phrase_display = []
        
        for char in self.phrase:
            self.phrase_list.append(char)
            if char == " ":
                self.phrase_display.append(" ")
            else:
                self.phrase_display.append(" _ ")
                
                
  def display(self, guesses):
      for letter in self.phrase:
        if letter in guesses:
          print(f"{letter} ", end="  ")
        else:
          print("_", end="  ")
          
          
      
  def check_letter(self, letter):
      letter in self.phrase_list
      for index, char in enumerate(self.phrase_list):
        if char ==letter:
          self.phrase[index] =letter
          return True
        else:
          return False

                                                                  
  def complete_check(self, guesses):
      for letter in self.phrase:
        if letter not in guesses:
          return True 
        else:
          return False