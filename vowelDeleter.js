const words = ['Slate', 'Earthy', 'Quick'];
let output = '';
for (var word of words) {
  word = word.toLowerCase();
  let tempWord = '';
  for (const letter of word) {
    if (!['a', 'e', 'i', 'o', 'u'].includes(letter)) {
      tempWord = tempWord.concat(letter, '');
    }
  }
  output = output.concat(tempWord, ' ');
}
console.log(output);
