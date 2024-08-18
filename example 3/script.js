document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('fade-in');
});

function changeDimension(num) {
    const container = document.querySelector("#container");
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }
    for (let i = 0; i < num; i++) {
        const div = document.createElement("div");
        container.appendChild(div);
    }
    let divs = document.querySelectorAll("#container div");
    divs.forEach(function(div) {
        div.style.flex = "1 1 calc(" + 100 / Math.sqrt(num) + "%)";
    });
}

function newPage() {
    const container = document.querySelector("#container");
    const divs = container.getElementsByTagName('div');
    for (let i = 0; i < divs.length; i++) {
        divs[i].style.backgroundColor = 'white';
    }
}

function eraser() {
    const container = document.querySelector("#container");
    let isMouseDown = false;

    const changeColor = (event) => {
        if (isMouseDown && event.target.tagName === 'DIV') {
            event.target.style.backgroundColor = '#ffffff';
        }
    };

    container.addEventListener('mousedown', (event) => {
        isMouseDown = true;
        changeColor(event);
    });
    container.addEventListener('mouseover', changeColor);

    document.addEventListener('mouseup', () => {
        isMouseDown = false;
    });
}

function coloring() {
    const container = document.querySelector("#container");
    const color = document.getElementById('color');
    let isMouseDown = false;

    const changeColor = (event) => {
        if (isMouseDown && event.target.tagName === 'DIV') {
            const colVal = color.value;
            event.target.style.backgroundColor = colVal;
        }
    };

    container.addEventListener('mousedown', (event) => {
        isMouseDown = true;
        changeColor(event);
    });
    container.addEventListener('mouseover', changeColor);

    document.addEventListener('mouseup', () => {
        isMouseDown = false;
    });
}
