const words = ["Software Engineer", "Student", "Nerd",  "Programmer"]
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

var basicTimeline = anime.timeline({
    autoplay: false
});

var pathEls = document.querySelectorAll(".check");
for (var i = 0; i < pathEls.length; i++) {
    var pathEl = pathEls[i];
    var offset = anime.setDashoffset(pathEl);
    pathEl.setAttribute("stroke-dashoffset", offset);
}

basicTimeline
    .add({
        targets: ".text",
        duration: 1,
        opacity: "0"
    })
    .add({
        targets: ".button",
        duration: 1300,
        height: 10,
        width: 300,
        backgroundColor: "#2B2D2F",
        border: "0",
        borderRadius: 100
    })
    .add({
        targets: ".progress-bar",
        duration: 2000,
        width: 300,
        easing: "linear"
    })
    .add({
        targets: ".button",
        width: 0,
        duration: 1
    })
    .add({
        targets: ".progress-bar",
        width: 80,
        height: 80,
        delay: 500,
        duration: 750,
        borderRadius: 80,
        backgroundColor: "#800080"
    })
    .add({
        targets: pathEl,
        strokeDashoffset: [offset, 0],
        duration: 200,
        easing: "easeInOutSine"
    });

document.querySelector(".button").addEventListener("click", function () {
    basicTimeline.play();
});

document.querySelector(".text").addEventListener("click", function () {
    basicTimeline.play();
});