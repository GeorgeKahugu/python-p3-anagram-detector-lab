# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word= word
    def match(self, word_list):
        sorted_word = sorted(self.word)
        return[word for word in word_list if sorted(word) == sorted_word]    
        pass