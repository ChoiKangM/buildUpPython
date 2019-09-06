print("안녕하세요!")
# 따옴표는 숫자가 아닌 문자
print("100")
# 문자열 뿐만 아니라, 숫자 출력도 가능
print(100)
# 값 여러 개를 콤마(,)로 구분하여 출력 가능
print(100, 200, 300)
# 치환 연산자, 포매팅 - 서식은 앞에 '%'가 붙음
print("%d" % 100)

# 응용
print("100 + 100")
print(100 + 100)
print("%d" % (100+100))

# print() 문자열 반환
# d, i, o, u 등 알아보자

# 서식 갯수와 %(구분자) 뒤에 나오는 숫자 개수가 같아야함
# print("%d" % (100,200))
# print("%d %d" % 100)

# print()에서 사용하는 서식
# %d, %x, %o, %f, %c, %s

# 이거 알고 있나?
# %.1f, %7.1f ,%5d, %05d, %10s 
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)
print("%g" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

# 문자열 출력
# 작은따옴표('), 큰따옴표(") 둘다 사용 가능
# 복수라인 출력 : '''...''' 또는 """...""" 사용

# 이스케이프 문자
# ₩newline, ₩₩, ₩', ₩" 등 알제?

# 변수 계산 및 출력
a = 100
b = 50
result = a + b
print(a)
print(b)
print(result)
print(a, b, result)
print(a, "+", b, "=", result)

# input() 함수 : 사용자로 부터 키보드 입력
# 입력받으면 문자열이니 상황에 따라type casting 필요 ex) int
print("Input your name: ")
name = input()
age = int(input("Input your age: "))
print("My name is %s" % name)
print("My age is %d" % age)

# format() 함수
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 7
print("I eat {0} apples".format(number))
print("I eat {num} apples".format(num=9))

print("%d %5d %05d" % (123, 123, 123))
# {}안의 0,1,2는 format()안의 0,1,2번째 값에 대응
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

# format 함수 정렬 : >(오른쪽정렬), <(왼쪽정렬), 숫자(전체자리수)
print('{:>5}'.format('123'))
print('{:>10}'.format('123'))
print('{:<10}'.format('123'))
print('{:<10}'.format('12.3'))
print('{:.3f}'.format(12.38898))
print('{:>05}'.format('123'))
print('{:>010}'.format('123'))