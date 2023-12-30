const words = ["Software Engineer", "Student", "Nerd"]
const dynameText = document.querySelector(".main h5");

let word_index = 0;
let char_index = 0;
let is_deleting = false;

const typeEffect = () => {
    const currentWord = words[word_index];
    const currentChar = currentWord.substring(0, char_index);
    dynameText.textContent = currentChar;

    if (!is_deleting && char_index < currentWord.length){
        char_index++;
        setTimeout(typeEffect, 200);
    } else if (is_deleting && char_index > 0){
        char_index--;
        setTimeout(typeEffect, 100);
    } else {
        is_deleting = !is_deleting;
        word_index = !is_deleting ? (word_index + 1) % words.length : word_index;
        setTimeout(typeEffect, 1200);
    }
}

typeEffect();