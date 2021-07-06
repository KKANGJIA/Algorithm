var twoSum = function(nums, target) {
    // console.log(nums.map((v, i) => nums.map((ano_v, ano_i) => v + ano_v == target && [i, ano_i] )))
    console.log(nums.reduce((a, c, i) => { 
        if (a + c == target) a.push(i) 
            return a; 
    }, []))
}

twoSum([2,7,11,15], 9);

//파이썬 풀이와 비슷한 풀이 
var twoSum = function(nums, target) {
    for (var i = 0; i < nums.length; i++) {
      for (var j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] === target) {
          return [i, j];
        }
      }
    }
  
    return []; // no answer
  };
   