// 정답 풀이
function solution(s) {
    return /^[0-9]+$/.test(s) && [4,6].includes(s.length);
  }
// 프로그래머스에서 \d 정규표현식을 지원하지 않아 저렇게 숫자로 했습니다. OR 조건에서 (s.length === 4 || s.length === 6) 대신 includes로 짧게 줄일 수 있다는 것 알아두세요.
// RegExp.prototype.test()
// test() 메서드는 주어진 문자열이 정규 표현식을 만족하는지 판별하고, 그 여부를 true 또는 false로 반환합니다.


//나의 풀이
function solution(s) {
  return s.length === 4 | 6 && /^[0-9]+$/.test(s)
}