class Grammar {
  constructor() {
    this.noun = [];
  }
  identify(sentence) { 
    const words = sentence.split(' ');
    for (let word of words) {
      let isNoun = false;
      for (let suffix of this.noun) {
        if (word.endsWith(suffix)) {
          console.log(word, ': noun');
          isNoun = true;
          break; 
        }
      }
      if (!isNoun) {
        console.log(word, ': not a noun');
      }
    }
  }
}
const grammar = new Grammar();
grammar.identify('Actor is smiling');