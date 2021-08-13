function solution(price, money, count) {
    const arrPrices = []; // 매회 이용금액을 저장할 배열
    for (let i=1; i<=count; i++){
        let currentPrice = price * i; //현재금액을 각각 구하고
        arrPrices.push(currentPrice); //배열에 각 금액 저장
    }
    const total = nextPrices.reduce((a,c)=>a+c); //금액의 총합을 구하고
    return total <= money ? 0 : total - money    //금액이 모자르면 차액을 리턴, 아니면 0 리턴
}

//15분 컷, 금액이 모자르지 않는 테케에 주의