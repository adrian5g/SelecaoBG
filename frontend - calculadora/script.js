const buttons = document.querySelectorAll('.btn');
const resultDisplay = document.querySelector('.result');
const historyDisplay = document.querySelector('.history');

const defaultFrontSize = resultDisplay.style.fontSize;

let currentOperator = '';
let firstNumber = '';
let secondNumber = '';

const df = new Intl.NumberFormat('pt-BR');

buttons.forEach((button) => {
  button.addEventListener('click', () => handleButtonClick(button.innerText));
});

window.addEventListener('keydown', (event) => handleButtonClick(event.key));

function handleButtonClick(key) {
  switch (key) {
    case '/':
    case '*':
    case '-':
    case '+':
      if (!firstNumber || firstNumber === 'Erro') return;

      currentOperator = key;
      updateDisplay();
      break;
    case 'AC':
    case 'c':
    case 'C':
    case 'Backspace':
      resetCalculator();
      break;
    case ',':
    case '.':
      if (firstNumber === 'Erro') return;

      if (currentOperator) {
        if (!secondNumber.includes('.')) secondNumber += '.';
      } else {
        if (!firstNumber.includes('.')) firstNumber += '.';
      }

      updateDisplay();
      break;
    case '=':
    case 'Enter':
      if (firstNumber && secondNumber && currentOperator) computeResult();
      break;
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
      if (firstNumber === 'Erro') return;

      if (currentOperator) {
        if (secondNumber.length < 12) secondNumber += key;
      } else {
        if (firstNumber.length < 12) firstNumber += key;
      }

      updateDisplay();
      break;
  }
}

function formatDisplay() {
  const num1 = parseFloat(firstNumber);
  const num2 = parseFloat(secondNumber);

  if (firstNumber.length > 12 || secondNumber.length > 12) {
    resultDisplay.style.fontSize = '32px';
  } else if (firstNumber.length > 6 || secondNumber.length > 6) {
    resultDisplay.style.fontSize = '40px';
  }

  return `${firstNumber ? df.format(num1) : ''} ${currentOperator} ${secondNumber ? df.format(num2) : ''}`;
}

function resetCalculator() {
  firstNumber = '';
  secondNumber = '';
  currentOperator = '';
  resultDisplay.innerText = '0';
  resultDisplay.style.fontSize = defaultFrontSize;
  historyDisplay.innerText = '';
}

function computeResult() {
  const num1 = parseFloat(firstNumber);
  const num2 = parseFloat(secondNumber);
  let result = 0;

  switch (currentOperator) {
    case '/':
      result = num2 !== 0 ? num1 / num2 : 'Erro';
      break;
    case '*':
      result = num1 * num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '+':
      result = num1 + num2;
      break;
  }

  historyDisplay.innerText = formatDisplay();
  firstNumber = `${result}`;
  secondNumber = '';
  currentOperator = '';
  updateDisplay();
}

function updateDisplay() {
  resultDisplay.innerText = formatDisplay().trim();
}
