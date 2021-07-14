function solution(n) {
    result = [];
    for(let i = 1; i <= n; i++) {
        if (n % i == 0) {
            result.push(i);
        }
    }
    console.log(result.reduce((a,c) => a+c));
}
solution(12)


// 한 줄로 끝내기
// function solution(n) {
//     return Array(n).fill().map((v, i) => i + 1).reduce((a, c) => n % c ? a : a + c, 0)
// }