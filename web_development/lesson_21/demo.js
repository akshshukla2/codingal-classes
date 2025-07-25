//methods

var c = "Akshita Shukla"

console.log(c.toLowerCase())
console.log(c.toUpperCase())
console.log(c.startsWith("Ak"))
console.log(Math.random())
console.log(Math.floor(21.7))


//loop

for (var i = 1; i < 11; i++) {
    console.log("No." + i)
}

//switch

var a = 3

switch (a) {
    case 1:
        console.log("Number is 1.")
        break;
    case 2:
        console.log("Number is 2.")
        break;
    case 3:
        console.log("Number is 3.")
        break;
    default:
        console.log("Other Number.")
}

//while

function reverseNumber(num) {

let reversedNum = 0;

while (num > 0) {

const remainder = num % 10;

reversedNum = reversedNum * 10 + remainder;

num = Math.floor(num / 10);

}

return reversedNum;

}

const number = 12345;

const reversedNumberResult = reverseNumber(number);

console.log(`Reversed number of ${number} is: ${reversedNumberResult}`);