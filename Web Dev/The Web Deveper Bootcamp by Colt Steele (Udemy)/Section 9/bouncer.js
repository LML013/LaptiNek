if (age < 0) {
	console.log("You haven't been born yet!")
}

else if(age < 18){
	console.log("Sorry, you are not old enough to enter the venue.");
}

else if(age < 21) {
	console.log("You can enter, but you cannot drink.");
};

else if(age == 21) {
	console.log("Happy 21st birthday!");
};

else {
	console.log("Come on in. You can drink.");
};

if ((age % 2) == 1) {
	console.log("Your age is odd!");
};

if (age % Math.sqrt(age) === 0) {
	console.log("Perfect Square!");
};