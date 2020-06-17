class Solution:
    def add(self, num1, num2):
        result = []
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        digitSum = 0
        digitCarry = 0
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0:
                digit1 = int(num1[index1])
            else:
                digit1 = 0
            if index2 >= 0:
                digit2 = int(num2[index2])
            else:
                digit2 = 0
            digitSum = digit1 + digit2 + digitCarry
            digitCarry = digitSum // 10
            digitSum = digitSum % 10
            result.insert(0, str(digitSum))
            index1 -= 1
            index2 -= 1
        if digitCarry > 0:
            result.insert(0, str(digitCarry))
        return "".join(result)

    def multiplyDigit(self, num1, digit2, digit2Log10):
        result = []
        index1 = len(num1) - 1
        digitProduct = 0
        digitCarry = 0
        while index1 >= 0:
            digit1 = int(num1[index1])
            digitProduct = digit1 * digit2 + digitCarry
            digitCarry = digitProduct // 10
            digitProduct = digitProduct % 10
            result.insert(0, str(digitProduct))
            index1 -= 1
        if digitCarry > 0:
            result.insert(0, str(digitCarry))
        result += ['0' for _ in range(digit2Log10)]
        return "".join(result)

    def multiply(self, num1: str, num2: str) -> str:
        listOfProducts = []
        index2 = len(num2) - 1
        digit2Log10 = 0
        while index2 >= 0:
            digit2 = int(num2[index2])
            listOfProducts.append(
                self.multiplyDigit(num1, digit2, digit2Log10)
            )
            index2 -= 1
            digit2Log10 += 1
        result = "0"
        for product in listOfProducts:
            result = self.add(result, product)
        indexResultStart = 0
        while indexResultStart < len(result) - 1 and \
                result[indexResultStart] == '0':
            indexResultStart += 1
        return result[indexResultStart:]
