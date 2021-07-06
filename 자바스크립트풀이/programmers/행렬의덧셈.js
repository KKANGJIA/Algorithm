function solution(arr1, arr2) {
    // 1. return과 {}를 expression과 같이 사용하는 경우 2. return과 {} 없이 단독 expression으로 사용
    //console.log(arr1.map((arr, i) => {return arr.map((v, j) => {return v + arr2[i][j]})}));
    console.log(arr1.map((arr, i) => arr.map((v, j) => v + arr2[i][j])));
}

solution([[1,2],[2,3]], [[3,4],[5,6]])
// 화살표 함수를사용할 때 코드 실행부분에 {} 사용하지 말기 
// 2차원 배열이기 때문에 반복문이 두 번 필요
// for을 안 쓰기로 했기 때문에 map을 두 번 연달아 사용
// map을 쓰는 이유는 1,2가 4,6으로, 2,3이 7,9로 1대1로 바뀌기 때문

// MDN참고
//화살표 함수 기본 구문
// (param1, param2, …, paramN) => { statements }
// (param1, param2, …, paramN) => expression
// 다음과 동일함:  => { return expression; }

// 매개변수가 하나뿐인 경우 괄호는 선택사항:
// (singleParam) => { statements }
// singleParam => { statements }

// 매개변수가 없는 함수는 괄호가 필요:
// () => { statements }

//화살표함수 고급구문 
// 객체 리터럴 표현을 반환하기 위해서는 함수 본문(body)을 괄호 속에 넣음:
// params => ({foo: bar})

// 나머지 매개변수 및 기본 매개변수를 지원함
// (param1, param2, ...rest) => { statements }
// (param1 = defaultValue1, param2, …, paramN = defaultValueN) => { statements }

// 매개변수 목록 내 구조분해할당도 지원됨
// var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
// f();  // 6



