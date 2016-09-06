function unique(arr){
	var res = arr.filter(function(item, idx, array){
		return idx === array.indexOf(item);
	});
	return res;
}

function unique1(a){
	return a.filter((el, i, arr)=>arr.indexOf(el)===i);
}

function unique2(a){
	return Array.from(new Set(a));  // ES 6
}

var a = [1, 1, '1', '2', 1];
// var ans = unique(a);
// var ans = unique1(a);
var ans = unique2(a)
console.log(ans); 