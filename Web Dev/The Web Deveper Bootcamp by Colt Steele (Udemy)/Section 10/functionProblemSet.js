// Write a function isEven() which takes a single numeric argument and
// returns true if the number is ever and false otherwise

function isEven(num) {
	return (num % 2 === 0);
}


// Write a function factorial() which takes a single numeric argument and
// returns the factorial of that number

function factorial(num) {
	if (num === 0) {
		return 1;
	}
	else {
		for (i = num - 1; i > 0; i--) {
			num *= i;
		}
		return num;
	}
}

// Write a runction kebabToSnake() which takes a single kebab-cased string argument and
// returns the snake_cased version.

function kebabToSnake(string) {
	return string = string.replace("-","_");
}