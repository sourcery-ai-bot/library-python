/* Highest order function to calculate two numbers given an operator */


function calculator(num1, num2, operator) {
    return operator(num1, num2);
}

function add(num1, num2) {
    return num1 + num2;
}

function subtract(num1, num2) {
    return num1 - num2;
}

function multiply(num1, num2) {
    return num1 * num2;
}

function divide(num1, num2) {
    return num1 / num2;
}

function raiseToPower(num1, num2) {
    return num1 ** num2;
}

function modulo(num1, num2) {
    return num1 % num2;
}

/* Create an array to contain each of the operators */
operators = [add, subtract, multiply, divide, raiseToPower, modulo]

/* Loop over each of the operators to invoke the functions on the operands
used as arguments  */
for (var i = 0; i < operators.length; i++) {
    answer = calculator(6, 2, operators[i])
    console.log(answer)
}
