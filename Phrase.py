class Phrase:
  
  
    def __init__(self, in_phrase):
        self.phrase = in_phrase.lower()
        self.phrase_list = []
        self.phrase_display = []
        for char in self.phrase:
            self.phrase_list.append(char)
            if char == " ":
                self.phrase_display.append(" ")
            else:
                self.phrase_display.append("_")
                
                
                
                

    def display(self):
        print(" ".join(self.phrase_display))
        
        
        

    def letter_check(self, in_letter):
        if in_letter in self.phrase_list:
            for index, char in enumerate(self.phrase_list):
                if char == in_letter:
                    self.phrase_display[index] = in_letter
            return True
        else:
            return False

          
          
          
    def complete_check(self):
        return "_" not in self.phrase_display