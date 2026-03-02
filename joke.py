import requests
import random
class Joke():
    def __init__(self, rand = True, word = None):
        self.rand = rand
        self.joke = ''
        self.word = word

    def get_joke_rand(self):
        try:
            base_url = 'https://icanhazdadjoke.com'

            headers = {'Accept': 'application/json', 'User-Agent' : 'Mylibrary https://github.com/EvgR7 '}
            par = {'limit': 1}
            data = requests.get(base_url, params=par, headers=headers)

            return data.json()['joke']

        except:
            return 'Somthing goes wrong'

    def get_joke_word(self, word):
        try:
            base_url = 'https://icanhazdadjoke.com/search'
            par = {'term': word, 'limit': 30}
            headers = {'Accept': 'application/json', 'User-Agent' : 'Mylibrary https://github.com/EvgR7 '}
            data = requests.get(base_url, params=par, headers=headers)

            return data.json()['results']

        except:
            return False

    def is_word(self, word):

        x = ['!','@','#','$','%','^',"*",':','(',')','/','1','2','3','4','5','6','7','8','9','0','<','>',";"]
        for i in x:
            if i in word:
                return False

        return True
    def make_a_word(self,word):
        if self.is_word(word):
            word = word.strip()
            word = word.lower()
            return word
        else:
            return False

    def return_rand_joke(self, word):
        good_word = self.make_a_word(word)
        if good_word == False:
            return 'Enter the word'
        results = self.get_joke_word(good_word)
        if results == False:
           return 'Somthing goes wrong'
        if results == []:
            return "Sorry, I can't find any joke, try another word"

        rand = random.randrange(0,len(results))
        return results[rand]['joke']