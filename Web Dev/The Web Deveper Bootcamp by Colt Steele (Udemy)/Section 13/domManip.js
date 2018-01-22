// Select h1
var h1 = document.querySelector("h1");
// Change h1 color to pink
h1.style.color = "pink";

// Select body
var body = document.querySelector("body");
var isBlue = false;

// Change background color every 5 seconds
setInterval(function() {
	if(isBlue) {
		body.style.background = "white";
	}	else {
		body.style.background = "blue";
	}
	isBlue = !isBlue;
}, 5000);