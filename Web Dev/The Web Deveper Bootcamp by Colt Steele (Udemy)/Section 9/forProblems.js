// Print all numbers between -10 and 19
console.log("Print all numbers between -10 and 19");
// var num1 = -10;

// while (num1 <= 19) {
// 	console.log(num1);
// 	num1++;
// };

for (var i = -10; i <= 19; i++) {
	console.log(i);
};

// Print all even numbers between 10 and 40
console.log("Print all even numbers between 10 and 40");
// var num2 = 10;

// while (num2 <= 40) {
// 	if (num2 % 2 === 0) {
// 		console.log(num2);
// 	};
// 	num2++;
// };

for (var i = 10; i <= 40; i++) {
	if (i % 2 === 0) {
		console.log(i);
	};
};

// Print all odd numbers between 300 and 333
console.log("Print all odd numbers between 300 and 333");
// var num3 = 300;

// while (num3 <= 333) {
// 	if (num3 % 2 === 1) {
// 		console.log(num3);
// 	};
// 	num3++;
// };

for (var i = 300; i <= 333; i++) {
	if (i % 2 !== 0) {
		console.log(i);
	};
};


// Print all numbers divisible by 5 AND 3 between 5 and 50
console.log("Print all numbers divisible by 5 AND 3 between 5 and 50");
// var num4 = 5;

// while (num4 <= 50) {
// 	if ((num4 % 5 === 0) && (num4 % 3 === 0)) {
// 		console.log(num4);
// 	};
// 	num4++;
// }

for (var i = 5; i <= 50; i++) {
	if ((i % 5 === 0) && (i % 3 === 0)) {
		console.log(i);
	};
};