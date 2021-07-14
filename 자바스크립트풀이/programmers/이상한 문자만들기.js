function solution(s) {
    return s.split(' ').map(w => (
        w.split('').map((v, i) => (
            i % 2 ? v.toLowerCase() : v.toUpperCase()
        )).join('')
      )).join(' ');
}

solution("try hello world");