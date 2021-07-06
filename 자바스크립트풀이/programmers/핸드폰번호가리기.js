'use strict'

function solution(phone_number) {
    console.log('*'.repeat(phone_number.length-4)+phone_number.slice(-4,))
}

phone_number = "01033334444"
phone_number = "027778888"

solution(phone_number)