import json

class posTagging :
    def __init__(self):
        try:
            self.treebank_dic = json.load(open('treebank_tagged_words', 'r'))
            self.wordnet_dic = json.load(open('wordnet_dictionary', 'r'))
            self.pos = json.load(open('pos.json','r'))
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        self.sentences = []
        self.words_types_list = []

    def parse(self, text):
        text = text.lower()
        current_sentence = ''

        for word in text.split():
            current_sentence += word + ' '
            if word[-1] in ('.', '!', '?'):
                self.sentences.append(current_sentence.strip())
                current_sentence = ''

        if current_sentence :
            self.sentences.append(current_sentence.strip())

        for sentence in self.sentences:
            for word in sentence.split():
                self.words_types_list.append(self.getWordType(word))

        return self.words_types_list

    def getWordType(self, word):
        types = set()
        if word[-1] in ('.', ',', ':', ';', '!', '?'):
            word = word[:-1]
            
        if '-' in word :
            types.add('Adjective')
            
        if word in self.treebank_dic:
            tag = self.treebank_dic[word]
            types.add(self.pos["TREEBANK_POS"].get(tag))
           
        elif word in self.wordnet_dic:
            pos_list = self.wordnet_dic[word]
            for pos in pos_list : 
                types.add(self.pos["WORDNET_POS"].get(pos))
                
        return {'word': word, 'type': list(types)}

tagger = posTagging()
print(tagger.parse('Either a boy or girl could sing.'))