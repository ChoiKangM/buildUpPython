# def로 함수 정의하지 않고, 간편하게 작성하여 사용
def plus_ten(x):
  return x + 10
plus_ten(1)

plus_ten = lambda x: x+10
plus_ten(1)

# 람다 표현식 자체를 바로 호출
(lambda x: x+10)(1)

# def 함수 + map 사용
list(map(plus_ten, [1,2,3]))

# lambda + map 사용
list(map(lambda x:x+10, [1,2,3]))

# lambda 표현식에 조건부 사용시 반드시 else 사용
list(map(lambds x:str(x) if x%3==0 else x, a))