const solution = (n) => {
    let answer = "";
    let restNum = 0;
  
    while (n > 0) {
      restNum = n % 3;
      n = Math.floor(n / 3);
      if (restNum == 0) {
        n -= 1;
        restNum = 4;
      }
      answer = restNum + answer;
    }
  
    return answer;
  };
  
  /*
  function solution(n) {
      return n ? solution((n - (n % 3 || 3)) / 3) + (n % 3 || 4): '';
  }
  */