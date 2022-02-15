from itertools import count
import string


class TextContainer():
    
    def __init__(self, my_text):
        self.my_text = my_text


    def count_words(self, my_string):
        result = len(my_string.split())
        print(result)

    def count_chars(self, my_string):
        result = len(my_string)
        print(result)    

    def count_ascii(self,my_string):
        ascii_string = string.ascii_letters
        ascii_count = sum(c in ascii_string for c in my_string)
        print(ascii_count)

    def contains_punctuation(self, my_string):
        strings = string.punctuation
        for i in my_string:
            if i in strings:
                my_string = my_string.replace(i,"")
        print(my_string)        
     

tc = TextContainer("jeg. 23, kan: 24; godt. 25, lide: 26; store. 27, katte: 28;")
#tc.count_words(tc.my_text)
#tc.count_chars(tc.my_text)
#tc.count_ascii(tc.my_text)
tc.contains_punctuation(tc.my_text)