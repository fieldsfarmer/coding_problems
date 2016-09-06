'use strict';

const news = [{len: 1, val: 2}, {len: 2, val: 3}, {len: 2, val: 1}, {len: 3, val: 2}];

function newsOfMaxVal(news, maxLength){
	if(maxLength == 0){
		return [];
	}
	var zeros = Array(maxLength+1).fill(0)
	var l = news.length;
	var dp = [];
	for(let i=0; i<=l; ++i){
		dp.push(zeros.slice(0));
	}
	for(let i=0; i<l; ++i){
		for(let j=0; j<=maxLength; ++j){
			if(i==0 || j==0){
				dp[i][j] = 0;
			}
			if(news[i].len > j){
				dp[i+1][j] = dp[i][j];
			}
			else{
				dp[i+1][j] = Math.max(dp[i][j], dp[i][j-news[i].len]+news[i].val)
			}
		}
	}
	console.log(dp)
	return dp[l][maxLength]
}

console.log(newsOfMaxVal(news, 4))