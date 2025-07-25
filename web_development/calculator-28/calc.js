const display = document.getElementById('display')
const buttons = document.querySelectorAll('.btn')

let currentInput = ''

const arithmeticRegex = /(\d+)\s*([-+*/])\s*(\d+)/;
function calculateExpression(expressionString) {
    // Attempt to match the regular expression against the input string.
    const match = expressionString.match(arithmeticRegex);
    if (match) {

        // If a match is found, extract the captured groups.

        // match[0] is the full matched string.

        // match[1] is the first number (Group 1).

        // match[2] is the operator (Group 2).

        // match[3] is the second number (Group 3).

        const num1 = parseFloat(match[1]); // Convert the first captured string to a float.

        const operator = match[2]; // The operator as a string.

        const num2 = parseFloat(match[3]); // Convert the second captured string to a float.

        let result;

        // Perform the arithmetic operation based on the extracted operator.

        switch (operator) {

            case '+':

                result = num1 + num2;

                break;

            case '-':

                result = num1 - num2;

                break;

            case '*':

                result = num1 * num2;

                break;

            case '/':

                // Handle division by zero to prevent errors.

                if (num2 === 0) {

                    return "Error: Division by zero is not allowed.";

                }

                result = num1 / num2;

                break;

            default:

                // This case should ideally not be reached if the regex is correct,

                // but it's good for robustness.

                return "Error: Unsupported operator found.";

        }

        return result;

    } else {

        // If no match is found, the string does not conform to the expected format.

        return "Error: Invalid expression format. Please use 'number operator number' (e.g., '10 + 5').";

    }

}

buttons.forEach(button => {

    button.addEventListener('click', () => {

        const value = button.innerText

        if (value == 'C') {

            currentInput = ''

            display.innerText = ''

        } else if (value == 'CE') {

            currentInput = currentInput.slice(0, -1)

            display.innerText = currentInput

        } else if (value == '=') {

            currentInput = calculateExpression(currentInput)

            display.innerText = currentInput

        } else {

            currentInput = currentInput + value
            display.innerText = currentInput
        }

    })
})