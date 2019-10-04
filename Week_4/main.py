import calculator

num1 = float(input("첫번째 숫자를 입력하세요 : "))
num2 = float(input("두번째 숫자를 입력하세요 : "))

print("더하기 : %.f" % calculator.plus(num1,num2))
print("빼기 : %.f" % calculator.minus(num1,num2))
print("곱하기 : %.f" % calculator.multiply(num1,num2))
print("나누기 : %.f" % calculator.divide(num1,num2))