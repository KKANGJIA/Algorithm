function solution(absolutes, signs) {
    const changeNum = []; 
    absolutes.map((v,i) => signs[i] ? changeNum.push(+v) : changeNum.push(-v))
    return changeNum.reduce((a,c)=>a+c)
}