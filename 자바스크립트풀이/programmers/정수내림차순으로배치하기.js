function solution(n) {
    return Number(String(n).split('').sort((x,y) => y - x).join(''));
}

solution(118372)

// 풀이 15분 소요

// function solution(n) {
//   return +String(n).split('').sort((p, c) => c - p).join('');
// }
// 앞에 +는 나머지 부분의 결과물로 나오는 문자열을 숫자로 바꾸는 것입니다.