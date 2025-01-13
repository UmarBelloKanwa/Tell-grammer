class Grammar {
  constructor() {
    this.words = '';
    this.sentences = [];
    this.words_types_list = [];
  }
  parse(text) {
    this.words = text.split(' ');
    let current_sentence = '';
    for (let word of this.words) {
      current_sentence += word + ' ';
      for (let pun of ['.', '!', '?']) {
        if (word.endsWith(pun)) {
          this.sentences.push(current_sentence.trim());
          current_sentence = '';
        }
      }
    }
    if (current_sentence.length > 0) {
      this.sentences.push(current_sentence.trim());
    }
    for (let sentence in this.sentences) {
      for (let word in sentence.split(' ')) {
        this.words_types_list.push(this.getWordType(word));
      }
    }
    return this.words_types_list;
  }
  getWordType(word) {
    const types = new Map();
    const request_dic = new XMLHttpRequest();
    word = word.toLowerCase();
    for (let pun of ['.', '!', '?']) {
      if (word.endsWith(pun)) {
        word.slice(-1);
      }
    }
    request_dic.onload = () => {
      let dictionary = JSON.parse(request_dic.responseText);
    }
    request_dic.open('GET', 'WordNet.json');
    request_dic.send();
    return types.entries();
  }
}
const grammar = new Grammar();
console.log(grammar.parse('I am Umar. How are you ? Are you well ! Great. It work C.B.N'));
