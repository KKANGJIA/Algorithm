'use strict'

// function solution(num) {
//     while (num > 1) {

//         let cnt = 0;

//         if (cnt == 500){
//             return -1;
//         } else if (num == 1) {
//             return cnt;
//         } else if (num != 1) {
//             if (num % 2 == 0) {
//                 num / 2;
//                 cnt++;
//             } else {
//                 num * 3 + 1;
//                 cnt++;
//             }
//         }
//     }       
// }

function solution(num, count = 0) {
    return count === 500 
        ? -1 
        : num === 1
            ? count
            : solution(num % 2 ? num * 3 + 1 : num / 2, count + 1);
}


solution(8)

// ctrl + shift + i 로 개발자 도구 열기