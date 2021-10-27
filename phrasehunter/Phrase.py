class Phrase:

  
  def __init__(self, phrase):
        self.phrases = phrase.lower()
      
        self.phrase_list = []
        self.phrase_display = []
        
        for char in self.phrases:
            self.phrase_list.append(char)
            if char == " ":
                self.phrase_display.append(" ")
            else:
                self.phrase_display.append(" _ ")
                
                
  def display(self, guesses):
      for letter in self.phrases:
            if letter == ' ':
                print(' ', end=' ')
            elif letter in guesses:
                print(f'{letter}', end="")
            else:
                print("_", end=" ")
          
          
      
  def check_letter(self, letter):
        if letter() in self.phrases:
            return True
        else:
            return False
    
                                                                  
  def complete_check(self, guesses):
      for letter in self.phrases:
            if letter not in guesses:
                return False
      return True