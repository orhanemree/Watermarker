const fileInput = [...document.querySelectorAll("input[type=file]")];
const fileText = [...document.querySelectorAll(".file-text")];

fileInput.forEach( el => {
    el.addEventListener("change", () => {
        const filename = el.files[0].name;
        fileText[fileInput.indexOf(el)].innerText = filename;
    });
});