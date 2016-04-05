'use strict';

function isPrime_simpleVersion (value) {
	if(value<=1) return false;
	// for(var i=2; i < value; ++i){
	for(var i=2; i*i <= value; ++i){
		if(value%i==0) return false;
	}
	return true;
}

// console.log(isPrime_simpleVersion(2));
// console.log(isPrime_simpleVersion(131));
// console.log(isPrime_simpleVersion(121));

function memorizedIsPrime(value){
	if(!memorizedIsPrime.values) memorizedIsPrime.values = {};
	if(memorizedIsPrime.values[value] !== undefined)
	// if(memorizedIsPrime.values.value !== undefined)
		return memorizedIsPrime.values[value];
	if(value<=1) memorizedIsPrime.values[value] = false;
	// for(var i=2; i < value; ++i){
	for(var i=2; i*i <= value; ++i){
		if(value%i==0){
			return memorizedIsPrime.values[value] = false;
			// memorizedIsPrime.values[value] = false;
			// return false;
		} 
	}
	return memorizedIsPrime.values[value] = true;
	// memorizedIsPrime.values[value] = true;
	// return true;	
}

function memorizedIsPrime2(value){
	if(!memorizedIsPrime2.values) memorizedIsPrime2.values = {};
	if(memorizedIsPrime2.values[value] !== undefined)
		return memorizedIsPrime2.values[value];
	// memorizedIsPrime2.values[value] = isPrime_simpleVersion(value);
	// return memorizedIsPrime2.values[value];
	return memorizedIsPrime2.values[value] = isPrime_simpleVersion(value);
}

Function.prototype.memorized = function(){
	if(!this.values) this.values = {};
	// var key = "";
	// for(let i=0; i<arguments.length; ++i){
	// 	key += arguments[i];
	// }
	var key = arguments[0];
	if(this.values[key] != undefined){
		return this.values[key];
	}
	// this.values[key] = this.apply(this, arguments);
	this.values[key] = this.call(this, arguments[0]);
	return this.values[key];
}

console.log(isPrime_simpleVersion.memorized(5), 'The function works; 5 is prime');
console.log(isPrime_simpleVersion.values[5], 'The answer is cached.');

Function.prototype.memorized1 = function(){
	var values = {},
		that = this;
	return function(){
		var key = arguments[0];
		if(values[key]!=undefined){
			return values[key];
		}
		// return values[key] = isPrime_simpleVersion(key);
		// return values[key] = that.call(this, key);
		return values[key] = that.call(null, key);
	}
}

var isPrime = isPrime_simpleVersion.memorized1();
console.log('17 is prime: ', isPrime(17));


var isPrimeScoped = (function(){
	var values = {};
	return function(value){
		if(values[value]!=undefined){
			return values[value];
		}
		return values[value] = isPrime_simpleVersion(value);
	}
}());

console.log('19 is prime: ', isPrimeScoped(17));
console.log('23 is prime: ', isPrimeScoped(23));
console.log('24 is prime: ', isPrimeScoped(24));


var test = [2, 3, 4, 5, 7, 7, 2, 3, 4, 4, 11, 121, 537];
var test2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 541];
var test3 = test2.concat(test2);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);
test3 = test3.concat(test3);

console.log(test3.length); // 827392


// var start1 = new Date().getMilliseconds();
var start1 = +new Date();
for(let j = 0; j<test3.length; ++j){
	isPrime_simpleVersion(test3[j])
}
// var end1 = new Date().getMilliseconds();
var end1 = +new Date();
console.log('isPrime_simpleVersion time taken: ' + (end1-start1)); // about 56

var start = +new Date();
for(let j = 0; j<test3.length; ++j){
	memorizedIsPrime(test3[j])
}
var end = +new Date();
console.log('memorizedIsPrime time taken: ' + (end-start)); // about 17

var start2 = +new Date();
for(let j = 0; j<test3.length; ++j){
	memorizedIsPrime2(test3[j])
}
var end2 = +new Date();
console.log('memorizedIsPrime2 time taken: ' + (end2-start2)); // about 19

var start3 = +new Date();
for(let j = 0; j<test3.length; ++j){
	isPrime_simpleVersion.memorized(test3[j])
}
var end3 = +new Date();
console.log('memorized  of Function.prototype time taken: ' + (end3-start3)); // about 23

var start4 = +new Date();
var isPrimeTest = isPrime_simpleVersion.memorized1();
for(let j = 0; j<test3.length; ++j){
	isPrimeTest(test3[j])
}
var end4 = +new Date();
console.log('memorized1 of Function.prototype time taken: ' + (end4-start4)); // about 23

var start5 = +new Date();
for(let j = 0; j<test3.length; ++j){
	isPrimeScoped(test3[j])
}
var end5 = +new Date();
console.log('isPrimeScoped time taken: ' + (end5-start5));     // about 17