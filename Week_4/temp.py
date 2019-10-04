def func1(x,y):
  return x+y

def func2(x,y,z):
  return x+y+z

sum = 0
lst = [10,20]
tpl = (10,20,30)

sum = func1(*lst)
print("func1 호출 결과 => %d" % sum)

sum = func2(*tpl)
print("func2 호출 결과 => %d" % sum)