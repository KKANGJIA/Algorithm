function solution(arr) {
    return arr.reduce((a, c) => a+c, 0) / arr.length;
}

solution([1, 2, 3, 4])
