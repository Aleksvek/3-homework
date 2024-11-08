import random


class Cipher:
    def __init__(self, *numbers):
        self._numbers = numbers

    def _perform_random_operation(self):
        if len(self._numbers) < 2:
            print("Для операции необходимо хотя бы два числа.")
            return None

        operation = random.choice(['+', '-', '*', '/'])
        num1, num2 = self._numbers[0], self._numbers[1]

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Ошибка: деление на ноль"
            else:
                result = num1 / num2

        return result

    def __str__(self):
        result = self._perform_random_operation()
        return f"Результат операции: {result}"

cipher = Cipher(12, 8)

print(cipher)
