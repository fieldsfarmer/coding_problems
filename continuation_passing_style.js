'use strict';

var $http = require('http');
// // The following is wrong, non-blocking!!!!
// function getY(){
// 	var y;
// 	$http.get('http://www.google.com/', function(jsonData){
// 		y = jsonData.y;
// 	})
// 	return y;
// }

// var x = 5,
// 	y = getY();
// console.log(x+y);  // NaN


function factorial(n){
	if(n==0)
		return 1;
	return n*factorial(n-1);
}

function factorial1(n, ret){
	if(n==0)
		ret(1);
	else
		factorial1(n-1, function(t0){
			ret(n*t0);
		});
}

function tailRecursionFac(n, a){
	if(n==0) return a;
	return tailRecursionFac(n-1, n*a);
}

function tailRecursionFac1(n, a, ret){
	if(n==0) ret(a);
	else
		tailRecursionFac1(n-1, a*n, ret);
}

console.log(factorial(10));
factorial1(10, function(n){console.log(n)});
console.log(tailRecursionFac(10, 1));
tailRecursionFac1(10, 1, function(n){console.log(n)});


var awhile = 100;

var x = 10,
	y = 0;

function getY(){
	y = 100;
}
setTimeout(getY, awhile);

console.log(x+y);  // 10

function getY1(continueWith){
	setTimeout(continueWith, awhile);
}

getY1(function(y){
	y = 100;
	console.log(x+y);
}); // 110

// -----------------------------------------------------

// function getY2(continueWith){
// 	$http.get('http://www.google.com/', function(jsonData){
// 		continueWith(jsonData.y);
// 	});
// }

// getY2(function(y){
// 	console.log(x+y);
// })



