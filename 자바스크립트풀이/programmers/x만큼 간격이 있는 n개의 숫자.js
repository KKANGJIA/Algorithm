"use strict"

function solution(x, n) {
    console.log(Array(n).fill(x).map((v, i) => (i + 1) * v))}
    
//Array.prototype.map은 콜백에 세 가지 인자를 전달합니다.
// 배열의 값, 값의 인덱스, 그리고 배열
// map으로 원래의 수와 배수를 1대1로 짝지어주기

solution(2, 5);
