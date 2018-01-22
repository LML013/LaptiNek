// Write a function printReverse() that takes an array as an argument
// and prints out the elements in the array in reverse order
// (don't actually reverse the array itself)

function printReverse(arr) {
	for (var i = arr.length - 1; i >= 0; i--) {
		console.log(arr[i]);
	}
}

// Write a function isUniform() which takes an array as an argument
// and returns true if all elements of the array are identical

function isUniform(arr) {
	for (var i = 1; i < arr.length; i++) {
		if(arr[i] !== arr[0]) {
			return false;
		} else {
			continue;
		}
	}
	return true;
}

// Write a function sumArray() that accepts an array of numbers
// and returns the sum of all numbers in the array

function sumArray(arr) {
	var answer = 0;
	arr.forEach(function(element) {
		answer += element;
	});
	return answer;
};

// Write a function max() that accepts an array of numbers
// and returns the maximum number in the array

function max(arr) {
	var answer = 0;
	arr.forEach(function(num){
		if (num > answer) {
			answer = num
		};
	});
	return answer;
};