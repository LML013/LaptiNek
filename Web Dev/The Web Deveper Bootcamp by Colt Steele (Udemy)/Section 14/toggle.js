// Toggle the body's background color between purple and white,
// when a button is clicked.
var button = document.querySelector("button");

button.addEventListener("click", function(){
	document.body.classList.toggle("green-bg");
});