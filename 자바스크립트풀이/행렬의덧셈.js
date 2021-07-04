function solution(arr1, arr2) {
    console.log(arr1.map((v, i) => {arr2.map((v, i) => {arr1[i] + arr2[i]})}))
    return arr1.map((arr, i) => arr.map((v, j) => v + arr2[i][j]));
}
// 2차원 배열이기 때문에 반복문이 두 번 필요
// for을 안 쓰기로 했기 때문에 map을 두 번 연달아 사용
// map을 쓰는 이유는 1,2가 4,6으로, 2,3이 7,9로 1대1로 바뀌기 때문
solution([[1,2],[2,3]], [[3,4],[5,6]])