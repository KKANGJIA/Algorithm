// function solution(x) {
//     console.log( x % (Number(String(x)[0])+Number(String(x)[1])) == 0 && true)
// }
// 채점 결과
// 정확성: 58.8
// 합계: 58.8 / 100.0
// 다른 테스트 케이스를 커버하지 못하는 이유: 3자리 수 등 자릿수를 정해놔서 그럼...ㅜㅜ

// //다른 풀이 방법
function solution(x) {
    console.log(!(x % String(x).split('').reduce((a, c) => a + c * 1, 0))) 
    console.log(String(x).split('').reduce((a, c) => a + c * 1 ))
}
// 자릿수를 쪼개서 더하는 건 split과 reduce
// x를 나눌 수 있으면 0(falsy value)가 나오기 때문에 앞에 !를 붙여 true로 만들었습니다. 
// 문자열을 숫자로 만들기 위해 이번에는 * 1을 한 번 붙여봤습니다. parseInt도 있고 +도 있고 / 1도 있고 다양하게 문자열을 숫자로 만들 수 있습니다.

solution(10)