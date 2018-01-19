function sing(){
    console.log("twinkle twinkle...");
    console.log("how i wonder...");
}

setInterval(sing(), 1000);

setInterval(function(){
	console.log("I am an anonymous function");
	console.log("THIS IS AWESOME!");
}, 2000)