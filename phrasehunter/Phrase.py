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
                
                
  def display(self):
        print(" ".join(self.phrase)) 
      
      
  def check_letter(self, letter):
        try: 
          letter in self.phrase_list
          for index, char in enumerate(self.phrase_list):
                if char ==letter:
                    self.phrase[index] =letter
          return True
        except KeyError:
          return False

                                                                  
  def complete_check(self):
        return "_" not in self.phrase