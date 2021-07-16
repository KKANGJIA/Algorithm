function solution(s, n) {
    const upper = 'ABCDEFGHIJKMLNOPQRSTUVWXYZ';
    // const lower = upper.toLowerCase();
    const arr_upper = upper.split('');
    // const arr_lower = lower.split('');
    
    s.split('').map((v,i) => {
        if (upper.split('')[i] === s.split('')[i]){
            if (s.split('')[i] === 'Z'){
                i = -1;
                console.log(arr_upper[i+n]);
            } else {
                console.log(arr_upper[i+n]);
            }
        }
    })
}

function solution(s, n) {
    return s.split('').map((l) => {
      return l === ' '
        ? l
        : l.charCodeAt() + n > 122 || (l.charCodeAt() <= 90 && l.charCodeAt() + n > 90)
          ? String.fromCharCode((l.charCodeAt() + n) - 26)
          : String.fromCharCode(l.charCodeAt() + n);
    }).join('');
}

solution('AB', 1)
// solution('Z', 1)