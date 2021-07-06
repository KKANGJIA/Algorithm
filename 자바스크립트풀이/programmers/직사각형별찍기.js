"use strict"

// process.stdin.setEncoding('utf8');
// process.stdin.on('data', data => {
//     const n = data.split(" ");
//     const a = Number(n[0]), b = Number(n[1]);
//     console.log(a);
//     console.log(b);
// });

function solution(a, b) {
    return Array(b).fill().map(() => '*'.repeat(a)).join('\n');
}

solution(5,3);