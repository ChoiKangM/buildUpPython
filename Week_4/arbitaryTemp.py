def func(*arg):
  result = 0
  for num in arg:
    result = result+num
  return result

sum = 0

sum = func(10,20)
print("매개변수 2개, 호출 결과 => %d" % sum)

sum = func(10,20,30)
print("매개변수 3개, 호출 결과 => %d" % sum)