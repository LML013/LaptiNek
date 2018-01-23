// Come up with 4 ways to select the first <p> tag [in selector-exercise.html].

var way1 = document.querySelector("p");
console.log(way1);

var way2 = document.getElementById("first");
console.log(way2);

var way3 = document.getElementsByTagName("p");
console.log(way3[0]);

var way4 = document.getElementsByClassName("special");
console.log(way4[0]);

var way5 = document.querySelector(".special");
console.log(way5);

var way6 = document.querySelector("#first");
console.log(way6);
