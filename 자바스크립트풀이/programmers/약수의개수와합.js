function solution(left, right) {
  const arr = Array(right-left+1).fill(left).map((v, i) => v + i)
  let result = 0; //총합
  
  arr.map( val => {
    let measure = []; //약수
    for(let i=1; i<=val; i++){
      val % i === 0 && measure.push(i);
    }
    measure.length % 2 ? result -= val : result += val;
  }); 
  return result;
}

solution(24,27);

function solution(left, right) {
  let result = 0; //총합
  
  for(let j=left; j<=right; j++){
    let measure = []; //약수
    for(let i=1; i<=j; i++){
      j % i === 0 && measure.push(i);
    }
    measure.length % 2 ? result -= j : result += j;
  } 
  return result;
}
