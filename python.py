import json
class Grammar :
  def __init__(self) :
    self.noun = json.load(open('noun_suffixes.json'))
  def identify(self, sentence) :
    words = sentence.split(' ')
    for word in words :
      isNoun = False
      for suffix in self.noun :
        if word.endswith(suffix) :
          print(word, ': noun')
          isNoun = True
          break
      if isNoun == False :
        print(word, ': not a noun')
grammar = Grammar()
grammar.identify(input())