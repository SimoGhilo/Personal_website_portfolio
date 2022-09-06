
//targets

let snake = document.getElementById("snake");
let space = document.getElementById("space");
let fortune = document.getElementById("fortune");

//elements to be changed

let figure1 = document.getElementById("figure1");
let figure2 = document.getElementById("figure2");
let figure3 = document.getElementById("figure3");

///Functions

function handleFigure1(){
    let display = figure1.getAttribute("display") || "block";
    figure1.style.display = display;
    display = display == "block" ? "none":"block";
    figure1.setAttribute("display",display);
};

 function handleFigure2(){
    let display = figure2.getAttribute("display") || "block";
    figure2.style.display = display;
    display = display == "block" ? "none":"block";
    figure2.setAttribute("display",display);
 };

 function handleFigure3(){
    let display = figure3.getAttribute("display") || "block";
    figure3.style.display = display;
    display = display == "block" ? "none": "block";
    figure3.setAttribute("display",display);
 };




 ///////////////////////////////////////////////////////

snake.addEventListener("click",handleFigure1);

space.addEventListener("click",handleFigure2);

fortune.addEventListener("click",handleFigure3);

















 